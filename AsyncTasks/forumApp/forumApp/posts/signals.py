from django.db.models.signals import post_save
from django.dispatch import receiver
from forumApp.posts.models import Post
from forumApp.posts.tasks import send_approval_email


@receiver(post_save, sender=Post)
def send_approval_notification(sender, instance, created, **kwargs):
    if not created and instance.approved:
        send_approval_email.delay(
            instance.author.username,
            instance.author.email,
            instance.title
        )
