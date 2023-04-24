from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserViewSerializer
from .models import VTUser
import random
import requests

# Create your views here.
def create_otp():
    return random.randint(1000, 9999)


def sms_send(a, msg):
    url = "https://2factor.in/API/V1/1793bfe6-a9f3-11ed-813b-0200cd936042/SMS/+91"+str(a[0])+'''/'''+str(msg)+'''/LFTESTUSER'''
    print(url)
    response = requests.request("GET", url)
    print(response.text)

@api_view(['POST'])
def user_signin(request):
    if request.method == 'POST':
        data = request.data
        otp = create_otp()
        data["otp"] = otp
        print(data['phone'])
        serializer = UserViewSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            sms_send([int(data["phone"])], str(otp))
            obj = VTUser.objects.get_by_natural_key(data["phone"])
            res = getattr(obj, "id")
            return Response({'msg': 'data created', 'userid': res})
        else:
            obj = VTUser.objects.get_by_natural_key(data["phone"])
            obj.otp = otp
            obj.save()
            sms_send([int(data["phone"])], str(otp))
            res = getattr(obj, "id")
            return Response({'msg': 'data created', 'userid': res})
