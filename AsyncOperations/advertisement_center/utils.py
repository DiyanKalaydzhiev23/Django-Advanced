from pathlib import Path
from math import ceil

from django.conf import settings
from redis import RedisError, Redis

from advertisement_center.choices import ProcessingStatus
from advertisement_center.models import Commercial

QUEUE_NAMES = ['heavy', 'light', 'default']


def get_video_metrics(video):
    file_extension = Path(video.name).suffix.lower().lstrip('.')  # mp4, mov
    size_in_mb = ceil(video.size / (1024 * 1024))
    duration_in_seconds = max(15, min(300, max(size_in_mb, 1) * 12))
    return file_extension, size_in_mb, duration_in_seconds

def stats_counts():
    return {
        'pending_count': Commercial.objects.filter(processing_status=ProcessingStatus.PENDING).count(),
        'completed_count': Commercial.objects.filter(processing_status=ProcessingStatus.COMPLETED).count(),
        'failed_count': Commercial.objects.filter(processing_status=ProcessingStatus.FAILED).count(),
        'processing_count': Commercial.objects.filter(processing_status=ProcessingStatus.PROCESSING).count(),
    }


def get_queue_sizes():
    try:
        redis_client = Redis.from_url(settings.CELERY_BROKER_URL)
        return {queue_name: redis_client.llen(queue_name) for queue_name in QUEUE_NAMES}
    except RedisError:
        return {queue_name: 'Unavailable' for queue_name in QUEUE_NAMES}