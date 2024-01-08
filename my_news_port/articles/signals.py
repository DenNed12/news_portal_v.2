from django.dispatch import receiver
from django.template.loader import render_to_string
from django.db.models.signals import m2m_changed
from articles.models import PostCategory
from sitedir.settings import SITE_URL,DEFAULT_FROM_EMAIL
from django.core.mail import  EmailMultiAlternatives
from articles.tasks import send_notifications
from django.db.models.signals import post_save
from articles.models import Post
from django.contrib.auth.models import User


@receiver(signal=post_save,sender=Post)
def notify_about_post(sender,instance, **kwargs):
    if kwargs['created']:
        preview = instance.preview()
        instance_id = instance.pk
        title = instance.title
        users = User.objects.all()
        print(preview,instance_id,users)
        for u in users:
            to_email = u.email
            send_notifications.delay(preview, instance_id, title, [to_email])

