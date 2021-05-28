from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    queryset = Post.objects.filter(status="published")
    context_object_name = "posts"
    paginate_by = 3
