from rest_framework import serializers
from api.models import Freelancers, Brand

# Serializer for the Freelancers model
class FreelancersSerializer(serializers.HyperlinkedModelSerializer):
    freelancer_id = serializers.ReadOnlyField()  # Read-only field for freelancer_id

    class Meta:
        model = Freelancers
        fields = "__all__"  # Serialize all fields of the Freelancers model

# Serializer for the Brand model
class BrandSerializer(serializers.HyperlinkedModelSerializer):
    brand_id = serializers.ReadOnlyField()  # Read-only field for brand_id

    class Meta:
        model = Brand
        fields = "__all__"  # Serialize all fields of the Brand model
