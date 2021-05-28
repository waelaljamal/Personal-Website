from django.contrib import admin

from .models import Post, CustomTag


@admin.register(CustomTag)
class CustomTagModelAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "background_color", "text_color"]
    list_editable = ["background_color", "text_color"]
    search_fields = ["id", "name", "slug"]
    prepopulated_fields = {"slug": ["name"]}


@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "tag_list",
        "status",
        "updated_at",
        "published_at",
    ]
    list_filter = ["status", "updated_at", "published_at"]
    search_fields = [
        "id",
        "title",
        "slug",
        "summary",
        "content",
        "tags__name",
        "status",
    ]
    date_hierarchy = "published_at"
    prepopulated_fields = {"slug": ["title"]}

    # https://django-taggit.readthedocs.io/en/latest/admin.html

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related("tags")

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())
