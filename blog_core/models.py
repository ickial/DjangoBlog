from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, related_name='blog_posts', on_delete=models.CASCADE)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def get_absolute_url(self):
        return reverse('blog-core:post_detail', args=[str(self.slug)])

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        post_str = 'MyPostObject:'
        return post_str + ' ' + self.title
