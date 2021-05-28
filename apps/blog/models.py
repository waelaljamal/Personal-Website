from django.db import models
from django.utils.timezone import datetime

from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase

from apps.core.abstract_models import AbstractTimeStamp


class CustomTag(TagBase):
    BACKGROUND_COLORS_CHOICES = (
        ("yellow", "yellow"),
        ("gray", "gray"),
        ("red", "red"),
        ("blue", "blue"),
        ("green", "green"),
        ("purple", "purple"),
        ("indigo", "indigo"),
    )

    TEXT_COLORS_CHOICES = (
        ("black", "black"),
        ("white", "white"),
    )

    background_color = models.CharField(
        choices=BACKGROUND_COLORS_CHOICES,
        default="yellow",
        max_length=10,
    )
    text_color = models.CharField(
        choices=TEXT_COLORS_CHOICES,
        default="black",
        max_length=10,
    )

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class TaggedWhatever(GenericTaggedItemBase):
    # Here is where you provide your custom Tag class.
    tag = models.ForeignKey(
        CustomTag,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_items",
    )


class Post(AbstractTimeStamp):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("published", "Published"),
    )

    title = models.CharField(max_length=150)
    slug = models.SlugField(unique=True)
    summary = models.TextField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to="posts/")

    tags = TaggableManager(through=TaggedWhatever, related_name="posts")

    status = models.CharField(
        choices=STATUS_CHOICES,
        default="published",
        max_length=10,
    )

    published_at = models.DateTimeField(default=datetime.now)

    class Meta:
        ordering = ["-published_at"]

    def __str__(self):
        return self.title[:50]
