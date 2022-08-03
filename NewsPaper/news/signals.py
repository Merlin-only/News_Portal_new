from django.db.models.signals import post_save
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import mail_managers
from .models import Subscribers


# в декоратор передаётся первым аргументом сигнал, на который будет реагировать эта функция, и в отправители надо передать также модель
@receiver(post_save, sender = Subscribers)
def notify_managers_appointment(sender, instance, created, **kwargs):
    if created:
        subject = f'{instance.user}'
    else:
        subject = f'Данные пользователя изменились {instance.user}'

    mail_managers(
        subject=subject,
        message=instance.message,
    )