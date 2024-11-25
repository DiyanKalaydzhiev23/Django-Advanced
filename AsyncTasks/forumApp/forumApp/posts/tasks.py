from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_approval_email(author_username, author_email, post_title):
    send_mail(
        subject='Your post has been approved',
        message=f'Hi {author_username}, \n\nYour post {post_title} has been approved!',
        from_email="forumAppEmail@forum.com",
        recipient_list=[author_email],
    )
