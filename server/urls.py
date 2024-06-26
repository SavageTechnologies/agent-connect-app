"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import path, include

from search.urls import site_urls as search_urls
from server.index_view import IndexView


def ping(request: HttpRequest) -> HttpResponse:
    return HttpResponse(content="PONG")


def admin_redirect(request: HttpRequest) -> HttpResponse:
    return redirect(to="./admin/", permanent=False)


urlpatterns = [
    path('ping', ping),
    path('ping/', ping),
    path('admin', admin_redirect),
    path('admin/', admin.site.urls),
    path("search/", include(search_urls)),
    path('', IndexView.as_view()),
    path('/', IndexView.as_view()),
]
