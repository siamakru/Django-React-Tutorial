"""
This code defines a serializer for the Django User model using Django REST Framework (DRF). 
It customizes how user data is serialized (converted to/from JSON) and how user instances are 
created from input data. 
"""

from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only":True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    


