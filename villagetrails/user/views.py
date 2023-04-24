from rest_framework.response import Response
from rest_flex_fields import FlexFieldsModelViewSet
from .serializers import UserViewSerializer
from VTToken.authentication import MultiTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from signin.models import VTUser
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class UserViewSet(FlexFieldsModelViewSet):
    serializer_class = UserViewSerializer
    authentication_classes = [MultiTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = VTUser.objects.all()
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['is_guest', 'id']

    def get_queryset(self):
        if self.kwargs.get('pk') not in [None, '', 0]:
            filteredUser = VTUser.objects.filter(id=self.kwargs.get('pk'))
            return filteredUser