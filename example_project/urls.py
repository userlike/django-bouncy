from django.urls import include, path
from django.contrib import admin

admin.autodiscover()
urlpatterns = [
    path("admin/", admin.site.urls),
    path("bouncy/", include("django_bouncy.urls")),
]
