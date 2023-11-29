from django.urls import path
from . import views

app_name = "blog-core"

urlpatterns = [
    path("posts/", views.post_list, name="post_list"),
    path("post_detail/<slug:post>", views.post_detail, name="post_detail"),
    path("posts/by_author/<str:username_str>", views.posts_by_author, name='posts_by_author'),
    path("posts/<int:year_str>/<int:month_str>/", views.posts_by_date, name='publish_date_posts')
]
