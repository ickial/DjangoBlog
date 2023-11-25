<<<<<<< HEAD
from django.urls import path
=======
# from django.conf.urls import url
# from . import views
#
# urlpatterns = [
#     # post views
#     url(r'^$', views.post_list, name='post_list'),
#     url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/'\
#         r'(?P<post>[-\w]+)/$',
#         views.post_detail,
#         name='post_detail'),
# ]
from django.urls import path, include
from django.contrib.auth import views as auth_views
>>>>>>> 6a8e41430f6f05a26f36ccb017254f0ce228ae1e
from . import views

app_name = "blog-core"

urlpatterns = [
    path("posts/", views.post_list, name="post_list"),
    path("post_detail/<int:post>", views.post_detail, name="post_detail"),
    path("posts/by_author/<str:username_str>", views.posts_by_author, name='posts_by_author'),
    path("posts/<int:year_str>/<int:mouth_str>", views.posts_by_date, name='publish_date_posts')
]
