"""
URL configuration for social_book project.

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
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from djoser import views as djoser_views
from .views import google_login_callback


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('login.html', views.login, name='login'),
    # path('register.html', views.register, name='register'),
    # path('index.html', views.index, name='index'),
    path('account/', include('account.urls')),
    path('dbtask/', include('dbtask.urls')),
    path('exceltask/', include('exceltask.urls')),
    path('excelpd/', include('excelpd.urls')),
    path('pdtasks/', include('pdtasks.urls')),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path('accounts/', include('allauth.urls')),
    path('accounts/google/login/callback/', google_login_callback, name='google_login_callback')
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)