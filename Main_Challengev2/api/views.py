from django.shortcuts import render
from rest_framework import viewsets, filters, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Freelancers, Brand
from api.serializers import FreelancersSerializer, BrandSerializer
from rest_framework.pagination import PageNumberPagination

# ViewSet for Freelancers model
class FreelancerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Freelancers.objects.all()  # Set the queryset to all Freelancers objects
    serializer_class = FreelancersSerializer  # Use the FreelancersSerializer for serialization

    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = super().get_queryset()  # Get the base queryset
        # Retrieve query parameters from the request
        first_name = self.request.query_params.get('first_name')
        last_name = self.request.query_params.get('last_name')
        email = self.request.query_params.get('email')
        phone_number = self.request.query_params.get('phone_number')
        followers = self.request.query_params.get('followers')

        # Filter the queryset based on the query parameters
        # /freelancers/?first_name=<Name>
        if first_name:
            queryset = queryset.filter(first_name=first_name)
        if last_name:
        # /freelancers/?last_name=<Name>
            queryset = queryset.filter(last_name=last_name)
        if email:
        # /freelancers/?email=<mail>
            queryset = queryset.filter(email=email)
        if phone_number:
        # /freelancers/?phone_number=<Number>
            queryset = queryset.filter(phone_number=phone_number)
        if followers:
        # /freelancers/?followers=<followers>
            queryset = queryset.filter(followers=followers)

        return queryset

# ViewSet for Brand model
class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()  # Set the queryset to all Brand objects
    serializer_class = BrandSerializer  # Use the BrandSerializer for serialization
