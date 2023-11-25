from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    context = {'published_posts': Post.objects.filter(status='published')}
    return render(request, 'published_posts.html', context)


def post_detail(request, post):
    get_object_or_404(Post, id=post, status='published')
    return render(request, 'post_detail.html', {'my_post': Post.objects.get(id=post, status='published')})


def posts_by_author(request, username_str):
    user_posts = Post.objects.filter(status='published', author__username=username_str)
    return render(request, 'posts_by_author.html', {'published_posts_by_author': user_posts})


def posts_by_date(request, year_str, mouth_str):
    posts_by_publish_date = Post.objects.filter(status='published', publish__year=year_str, publish__month=mouth_str)
    return render(request, 'posts_by_date.html', {'posts': posts_by_publish_date})
