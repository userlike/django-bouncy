"""URLs for the Django-Bouncy App"""
from django.urls import path
# pylint: disable=invalid-name
from django_bouncy.views import endpoint

urlpatterns = [
    path('', endpoint)
]
