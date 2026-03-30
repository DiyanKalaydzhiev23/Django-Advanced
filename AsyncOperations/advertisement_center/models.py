from django.db import models

from advertisement_center.choices import ProcessingStatus, VideoFormat
from advertisement_center.validators import validate_video_upload


class Commercial(models.Model):
    slogan = models.CharField(
        max_length=150,
    )
    body = models.TextField()
    video = models.FileField(
        upload_to='commercial_videos/%Y/%m/%d/',
        validators=[validate_video_upload]
    )
    processing_status = models.CharField(
        choices=ProcessingStatus.choices,
        max_length=20,
        default=ProcessingStatus.PENDING,
        db_index=True,
    )
    video_duration = models.PositiveIntegerField(
        default=0
    )
    video_format = models.CharField(
        max_length=10,
        choices=VideoFormat.choices,
        blank=True,
        default='',
    )
    size_in_mb  = models.PositiveIntegerField(
        default=0
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )