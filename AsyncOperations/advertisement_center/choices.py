from django.db import models


class ProcessingStatus(models.TextChoices):
    PROCESSING = 'processing', 'Processing'
    PENDING = 'pending', 'Pending'
    COMPLETED = 'completed', 'Completed'
    FAILED = 'failed', 'Failed'


class VideoFormat(models.TextChoices):
    MP4 = 'mp4', 'MP4'
    MOV = 'mov', 'MOV'
    MKV = 'mkv', 'MKV'
