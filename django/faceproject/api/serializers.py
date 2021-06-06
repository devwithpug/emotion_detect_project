from rest_framework import serializers
from .models import Face
from django.contrib.auth.models import User


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'email')


class FaceSerializer(serializers.ModelSerializer):
    content = serializers.JSONField(required=True)

    class Meta:
        model = Face
        fields = (
            'content',
            'result',
        )
        read_only_fields = ('result',)


