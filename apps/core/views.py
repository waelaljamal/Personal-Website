from django.views.generic import TemplateView

from apps.blog.models import Post


class IndexView(TemplateView):
    template_name = "core/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Post.objects.filter(status="published")[:3]
        return context
