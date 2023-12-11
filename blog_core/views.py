from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'blog/post/published_posts.html'


def post_list(request):
    object_list = Post.objects.filter(status='published')
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request,'published_posts.html',{'page': page,'posts': posts})


def post_detail(request, post):
    get_object_or_404(Post, slug=post, status='published')
    return render(request, 'post_detail.html', {'my_post': Post.objects.get(slug=post, status='published')})


def posts_by_author(request, username_str):
    user_posts = Post.objects.filter(status='published', author__username=username_str)
    return render(request, 'posts_by_author.html', {'published_posts_by_author': user_posts})


def posts_by_date(request, year_str, month_str):
    posts_by_publish_date = Post.objects.filter(status='published', publish__year=year_str, publish__month=month_str)
    return render(request, 'posts_by_date.html', {'posts': posts_by_publish_date})
