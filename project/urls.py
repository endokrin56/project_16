"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.template.defaulttags import url
from django.urls import path, include

from app.views import UsersresList

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('pages/', include('django.contrib.flatpages.urls')),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('account/', include("accounts.urls")),  # Добавили эту строчку
    path('accounts/', include("allauth.urls")),
    path('apps/', include('app.urls')),
    path('', include('app.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('usersresponse/<int:article>', UsersresList.as_view(), name='usersres_list'),
    path('usersresponse/',  include('app.urls')),
    #url(r'^accounts/', include('registration.backends.simple.urls')),
]

#urlpatterns = [
    #url('^', include('django.contrib.auth.urls')),
    #url('^', include('pages.urls')),
    #url(r'^pages/', include('pages.urls')),
    #url(r'^search/', include('search.urls')),
    #url(r'^admin/', admin.site.urls),
#]