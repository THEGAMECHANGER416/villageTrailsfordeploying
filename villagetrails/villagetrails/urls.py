"""aaoSeekheinBackEnd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from signin.views import user_signin
from VTToken.views import get_token
from user.views import UserViewSet
from listing.views import ListingViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('villagetrails/v1/signin', user_signin),
    path('villagetrails/v1/gettoken', get_token),
    path('villagetrails/v1/user', UserViewSet.as_view({'get': 'list', 'patch': 'partial_update'})),
    path('villagetrails/v1/user/<int:pk>', UserViewSet.as_view({'get': 'list', 'patch': 'partial_update'})),
    path('villagetrails/v1/listing/', ListingViewSet.as_view({'get': 'list', 'post':'create', 'patch': 'partial_update'})),
    path('villagetrails/v1/listing/<int:pk>',
         ListingViewSet.as_view({'get': 'list', 'post': 'create', 'patch': 'partial_update'})),

]
