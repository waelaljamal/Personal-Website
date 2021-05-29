from django import template


register = template.Library()


@register.inclusion_tag('blog/includes/_posts.html')
def load_posts_summary(posts):
    return {'posts': posts}
