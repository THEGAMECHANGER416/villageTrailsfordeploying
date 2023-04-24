from rest_framework.serializers import ModelSerializer
from .models import Listing
from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer
from user.serializers import UserViewSerializer

class ListingSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'id', 'name', 'description', 'state', 'isActive', 'startDate', 'endDate', 'hostId','guestId', 'cost', 'createdAt'
        ]
        expandable_fields = {
            'hostId': (UserViewSerializer),
            'guestId': (UserViewSerializer)
        }
        # depth = 1
