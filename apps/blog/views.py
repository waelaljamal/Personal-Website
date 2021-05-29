from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from .models import Post, CustomTag


class BlogBaseMixin(ListView):
    queryset = Post.objects.filter(status="published")
    context_object_name = "posts"
    paginate_by = 3


class PostListView(BlogBaseMixin):
    pass


class TagView(BlogBaseMixin):
    template_name = "blog/tag_detail.html"

    def get_queryset(self, **kwargs):
        quertset = super().get_queryset(**kwargs)
        tag = get_object_or_404(CustomTag, slug=self.kwargs.get("slug"))
        return quertset.filter(tags__in=[tag])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = get_object_or_404(CustomTag, slug=self.kwargs.get("slug"))
        return context
