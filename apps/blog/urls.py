from django.urls import path

from .views import PostListView, TagView

app_name = "blog"

urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("tags/<slug:slug>/", TagView.as_view(), name="tag_detail"),
]
