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
from . import views

app_name = "blog-core"

urlpatterns = [
    path("posts/", views.post_list, name="post_list"),
    path("post_detail/<int:post>", views.post_detail, name="post_detail"),
]