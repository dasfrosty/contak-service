"""
server root URL Configuration
"""
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path("", RedirectView.as_view(url="/contak/")),
    path("admin/", admin.site.urls),
    path("contak/", include("contak.urls")),
]
