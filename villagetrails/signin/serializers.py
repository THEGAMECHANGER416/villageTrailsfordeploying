from rest_framework.serializers import ModelSerializer
from .models import VTUser


class UserViewSerializer(ModelSerializer):
    class Meta:
        model = VTUser
        fields = ['id', 'phone', 'name','is_guest', 'createdAt','otp']