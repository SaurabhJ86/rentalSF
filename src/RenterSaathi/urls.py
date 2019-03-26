"""RenterSaathi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include,path
from django.views.generic import TemplateView

from homepage.views import (
    createListPropertyAD,
    homepage,
    getContact,
    listProperty,
    owner,
    showProperty,
    )

urlpatterns = [
	path('', homepage, name='home'),
	path('getContact/',getContact.as_view(),name='getContact'),
	path('owner/',owner,name='owner'),
    path('owner/listings/',listProperty,name='listProperty'),
    path('admin/', admin.site.urls),
    path('listProperty/',createListPropertyAD,name='listPropertyUser'),
    path('listProperty/<int:id>/',showProperty,name='showProperty'),
    path('about/',TemplateView.as_view(template_name='about.html'),name='about'),
    path('hostel/',include('hostel.urls',namespace="hostel")),
    path('profile/',include('Profile.urls',namespace='Profile')),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)