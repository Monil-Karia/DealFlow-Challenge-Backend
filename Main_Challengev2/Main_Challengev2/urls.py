"""
URL configuration for Main_Challengev2 project.

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
from Main_Challengev2 import views

# URL patterns for the application
urlpatterns = [
    path("admin/", admin.site.urls),  # URL pattern for Django admin interface
    path("api/v1/", include('api.urls')),  # URL pattern for API endpoints
    path("", views.home_page),  # URL pattern for the home page
]

