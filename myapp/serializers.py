from rest_framework import serializers
from .models import Student


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields = ["email","password"]