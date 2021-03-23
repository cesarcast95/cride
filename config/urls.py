"""Main URLs module."""

from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin

#import ipdb; ipdb.set_trace() ##para interactuar con el debugger
urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
