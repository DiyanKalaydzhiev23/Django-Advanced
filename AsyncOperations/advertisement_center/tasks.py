import logging
import time
from datetime import timedelta

from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone

from advertisement_center.choices import ProcessingStatus
from advertisement_center.models import Commercial
from advertisement_center.utils import get_video_metrics

logger = logging.getLogger(__name__)


def enqueue_video_processing(commercial_id, queue):
    try:
        if queue == "light":
            return refresh_commercial_slogan.apply_async(args=[commercial_id], queue=queue)
        else:
            return process_commercial_video.apply_async(args=[commercial_id], queue=queue)
    except Exception:
        Commercial.objects.filter(pk=commercial_id).update(
            processing_status=ProcessingStatus.FAILED,
        )
        logger.exception(f'Commercial {commercial_id} failed permanently')
        return None


@shared_task(bind=True, max_retries=3, default_retry_delay=10)
def process_commercial_video(self, commercial_id: int):
    try:
        commercial = Commercial.objects.get(pk=commercial_id)
    except Commercial.DoesNotExist:
        logger.warning(f'Commercial {commercial_id} does not exist')
        return {'status': 'missing', 'commercial_id': commercial_id}

    Commercial.objects.filter(pk=commercial_id).update(
        processing_status=ProcessingStatus.PROCESSING,
    )
    logger.info(f'Commercial {commercial_id} is processing')

    try:
        if not commercial.video:
            raise ValueError('A video file is required before processing can start')

        if 'fail' in commercial.video.name.lower():
            raise ValueError('Simulated failure triggered by the uploaded file name')

        time.sleep(10)  # simulate a really complex task

        file_extension, size_in_mb, duration_in_seconds = get_video_metrics(commercial.video)

        Commercial.objects.filter(pk=commercial_id).update(
            processing_status=ProcessingStatus.COMPLETED,
            video_format=file_extension,
            size_in_mb=size_in_mb,
            video_duration=duration_in_seconds
        )

        send_mail(
            subject='Commercial Video upload finished',
            message=(
                f'Slogan: {commercial.slogan}'
                f'Format: {file_extension}'
                f'Duration: {duration_in_seconds}'
                f'Size: {size_in_mb}MB'
            ),
            recipient_list=['student@example.com'],
            from_email=settings.DEFAULT_FROM_EMAIL,
            fail_silently=True,
        )

        logger.info(f'Commercial {commercial_id} is processed successfully!')
        return {
            'status': ProcessingStatus.COMPLETED,
            'commercial_id': commercial_id,
            'video_format': file_extension,
            'duration_in_seconds': duration_in_seconds,
            'size': size_in_mb,
        }
    except Exception as exc:
        if self.request.retries >= self.max_retries:
            Commercial.objects.filter(pk=commercial_id).update(
                processing_status=ProcessingStatus.FAILED,
            )
            logger.exception(f'Commercial {commercial_id} failed permanently!')
            raise

        Commercial.objects.filter(pk=commercial_id).update(
            processing_status=ProcessingStatus.PENDING,
        )

        raise self.retry(exc=exc, countdown=min(60, 5 * (self.request.retries + 1)))


@shared_task(bind=True)
def refresh_commercial_slogan(self, commercial_id: int):
    commercial = Commercial.objects.get(pk=commercial_id)
    commercial.slogan = ' '.join(word.capitalize() for word in commercial.slogan.split())
    commercial.save(update_fields=['slogan'])
    logger.info(f'Commercial {commercial_id} slogan was normalized!')
    return {'status': 'updated', 'commercial_id': commercial_id, 'slogan': commercial.slogan}


@shared_task(bind=True)
def delete_old_commercials(self):
    cutoff = timezone.now() - timedelta(minutes=settings.COMMERCIAL_RETENTION_MINUTES)
    commercials = Commercial.objects.filter(created_at__lt=cutoff)
    deleted_count = commercials.count()

    for commercial in commercials:
        if commercial.video:
            commercial.video.delete(save=False)

    commercials.delete()
    logger.info(f'Deleted {deleted_count} commercials')
    return {'deleted_count': deleted_count, 'cutoff': cutoff.isoformat()}