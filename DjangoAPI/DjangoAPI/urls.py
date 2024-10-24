"""
URL configuration for DjangoAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from apli.home.home_view import home_view
from apli.login.login_view import (
    login_view, registro_view, olvide_view,
    detalles_view, video_view, blog_details_view, blog_view,
    logout_view
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registro_view, name='registro'),
    path('forgot_password/', olvide_view, name='olvide'),
    path('anime_details/', detalles_view, name='detalles'),
    path('watching/', video_view, name='videos'),
    path('blog/', blog_view, name='blog'),
    path('blog_details/', blog_details_view, name='blog_detalles'),
    path('', home_view, name='home'),
    path('home/', home_view, name='home'),
]
