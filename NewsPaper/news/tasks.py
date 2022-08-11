from celery import shared_task
from django.db.models.signals import post_save
from django.core.mail import mail_managers
from .models import Post
from django.dispatch import receiver


@shared_task (name='send_email_add_news')
@receiver(post_save, sender = Post)
def send_email_add_news(sender, instance, created, **kwargs):
    if created:
        subject = f'Появилась новая статья {instance.title_post}'
    else:
        subject = f'Отредактирована статья {instance.title_post}'
    mail_managers(
        subject=subject,
        message=instance.message,
    )

@shared_task (name='send_email_week')
def send_email_week()
    news_list = list(Post.objects.all().exclude(time_in__gt = datetime.now() - timedelta(day = 7)))
    news_list.save()

    mail_managers(
        subject=f'Последние новости {news_list}',
        message=instance.message,
    )
