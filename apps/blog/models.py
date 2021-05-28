from django.db import models
from django.utils.timezone import datetime

from taggit.managers import TaggableManager

from apps.core.abstract_models import AbstractTimeStamp


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

    tags = TaggableManager()

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
