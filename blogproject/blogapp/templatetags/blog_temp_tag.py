from blogapp.models import Post
from django import template#we should register our own template tags with template library so need to import template from django
register=template.Library()

@register.simple_tag(name='my_tag')
def total_posts():
    return Post.objects.count()
@register.inclusion_tag('blogapp/latests123.html')
def show_latest_posts(count=3):
    latest_posts=Post.objects.order_by('-publish')[:count]
    return {'latest_posts':latest_posts}
from django.db.models import Count

@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')
