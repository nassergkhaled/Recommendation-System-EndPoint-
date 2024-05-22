from rest_framework import serializers
from .models import User, Apartment, UserInteraction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'preferences']

class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = ['id', 'title', 'description', 'price', 'recommended_score']

class UserInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInteraction
        fields = ['id', 'user', 'apartment', 'rating']

