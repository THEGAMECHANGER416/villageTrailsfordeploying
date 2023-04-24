from signin.models import VTUser
from rest_flex_fields.serializers import FlexFieldsModelSerializer


class UserViewSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = VTUser
        fields = ['id', 'name', 'phone', 'is_guest', 'createdAt']
        depth = 1

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
