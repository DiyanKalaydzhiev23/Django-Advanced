from datetime import timezone
from pathlib import Path
from math import ceil
from celery import current_app
from django.conf import settings
from redis import Redis, RedisError

from advertisement_center.choices import ProcessingStatus
from advertisement_center.models import Commercial


QUEUE_NAMES = ('default', 'heavy', 'light')


def get_video_metrics(video):
    file_extension = Path(video.name).suffix.lower().lstrip('.')
    file_size_bytes = video.size if video else 0
    size_in_mb = ceil(file_size_bytes / (1024 * 1024)) if file_size_bytes else 0
    duration_in_seconds = max(15, min(300, max(size_in_mb, 1) * 12))
    return file_extension, size_in_mb, duration_in_seconds


def status_counts():
    return {
        'pending_count': Commercial.objects.filter(processing_status=ProcessingStatus.PENDING).count(),
        'processing_count': Commercial.objects.filter(processing_status=ProcessingStatus.PROCESSING).count(),
        'completed_count': Commercial.objects.filter(processing_status=ProcessingStatus.COMPLETED).count(),
        'failed_count': Commercial.objects.filter(processing_status=ProcessingStatus.FAILED).count(),
        'auto_refresh_ms': 4000,
    }


def get_queue_sizes():
    try:
        redis_client = Redis.from_url(settings.CELERY_BROKER_URL)
        # {light: 3, heavy: 5, default: 0}
        return {queue_name: redis_client.llen(queue_name) for queue_name in QUEUE_NAMES}
    except RedisError:
        return {queue_name: 'Unavailable' for queue_name in QUEUE_NAMES}


def running_tasks():
    inspect = current_app.control.inspect(timeout=1.0)
    active_tasks = inspect.active() if inspect else {}

    _running_tasks = []
    for worker_name, worker_tasks in (active_tasks or {}).items():
        for task in worker_tasks:
            _running_tasks.append(
                {
                    'worker': worker_name,
                    'name': task.get('name', 'n/a'),
                    'id': task.get('id', 'n/a'),
                    'args': task.get('argsrepr') or task.get('args') or '[]',
                }
            )
    return _running_tasks
