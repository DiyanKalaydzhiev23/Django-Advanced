import math
from pathlib import Path

from django.core.exceptions import ValidationError

from advertisement_center.choices import VideoFormat


VIDEO_SIZE_LIMITS_MB = {
    VideoFormat.MP4: 100,
    VideoFormat.MKV: 250,
    VideoFormat.MOV: 150,
}


def validate_video_upload(uploaded_file):
    if not uploaded_file:
        return

    extension = Path(uploaded_file.name).suffix.lower().lstrip('.')
    if extension not in VIDEO_SIZE_LIMITS_MB:
        supported_formats = ', '.join(choice.value for choice in VideoFormat)
        raise ValidationError(f'Unsupported video format. Choose one of the following: {supported_formats}')

    size_in_mb = math.ceil(uploaded_file.size / (1024 * 1024)) if uploaded_file.size else 0
    allowed_size = VIDEO_SIZE_LIMITS_MB[extension]
    if size_in_mb > allowed_size:
        raise ValidationError(f"{extension.upper()} files may be at most {allowed_size}MB.")
