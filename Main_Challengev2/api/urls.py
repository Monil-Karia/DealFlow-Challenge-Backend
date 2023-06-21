from django.contrib import admin
from django.urls import path, include
from api.views import FreelancerViewSet, BrandViewSet
from rest_framework import routers

# Creating a router instance
router = routers.DefaultRouter()

# Registering the viewsets with the router
router.register(r'freelancers', FreelancerViewSet)
router.register(r'brands', BrandViewSet)

# URL patterns for the API endpoints
urlpatterns = [
    # Including the router URLs
    path('', include(router.urls))
]

