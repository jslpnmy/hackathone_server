from rest_framework import serializers
from .models import User, Message, SignLogin


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['message']


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignLogin
        fields = ['name', 'email', 'password']
