from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import ListingSerializer
from VTToken.authentication import MultiTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Listing
# from signin import VTUser
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class ListingViewSet(ModelViewSet):
    queryset = Listing.objects.all().order_by('-createdAt')
    serializer_class = ListingSerializer
    authentication_classes = [MultiTokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    filterset_fields = []
    ordering_fields = ['createdAt']

    def get_queryset(self):
        req = self.request
        all_objects = Listing.objects.all()
        if req.query_params.dict().get('guestId') not in [None, '', ' ', 'null']:
            guestId = int(req.query_params.dict().get('guestId'))
            print("guestId", guestId)
            if guestId != 1:
                filter_dishes = all_objects.filter(guestId__id=guestId)
                return filter_dishes
        if req.query_params.dict().get('hostId') not in [None, '', ' ', 'null']:
            hostId = int(req.query_params.dict().get('hostId'))
            print("hostId", hostId)
            if hostId != 0:
                filter_dishes = all_objects.filter(hostId__id=hostId)
                return filter_dishes
        else:
            if self.kwargs.get('pk') not in [None, '', 0]:
                filteredListing = Listing.objects.filter(id=self.kwargs.get('pk'))
                return filteredListing
            return self.queryset




