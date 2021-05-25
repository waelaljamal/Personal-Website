from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path("", include("app.urls")),
]

if settings.DEBUG:
    if "silk" in settings.INSTALLED_APPS:
        urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
