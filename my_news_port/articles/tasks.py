from articles.models import Post,Category
from celery import shared_task
from sitedir.settings import DEFAULT_FROM_EMAIL
from  django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from sitedir.settings import SITE_URL
from datetime import datetime
@shared_task
def send_notifications(preview, pk, title, to_email):
    html_content = render_to_string(
        'post_created_email.html',
        {
            'text': preview,
            'link': f'{SITE_URL}/news/{pk}',
        }
    )
    msg = EmailMultiAlternatives(
        subject=title,
        body='',
        from_email=DEFAULT_FROM_EMAIL,
        to=to_email,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.encoding = 'utf-8'
    msg.send()


@shared_task
def send_weekly_articles():
    today = datetime.datetime.now()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(added_at__gte = last_week)
    categories = set(posts.values_list('postCategory__name', flat= True ))
    subscribers = set(Category.objects.filter(name__in =categories).values_list('subscribers_email'))
    print(subscribers)

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': SITE_URL,
            'posts': posts
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body=' ',
        from_email= DEFAULT_FROM_EMAIL,
        to = subscribers
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
