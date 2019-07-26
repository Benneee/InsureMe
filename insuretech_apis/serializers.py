from django.contrib.auth.models import User, Group
from rest_framework import serializers, viewsets
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class ProfileLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = AInsuranceUserProfile
        fields = '__all__'  # ['username','password']


class AInsuranceUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = AInsuranceUserProfile
        fields = '__all__'
        # exclude = ['token','registrationdate',]


class AUserbankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AUserbankDetails
        fields = ['insuranceuserprofile', ]


class AUserworkDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AUserworkDetails
        fields = ['insuranceuserprofile', ]


class AMotorInsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = AMotorInsurance
        fields = ['insuranceuserprofile', ]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['username',  'linenos', 'created']


# class TipsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Tips
#         fields = ['tip', 'insurance_type']

class TipsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tips
        fields = ['tip',]



class GeneralTipsViewSet(viewsets.ModelViewSet):
    queryset = Tips.objects.filter(insurance_type="general")
    serializer_class = TipsSerializer


class AutoTipsViewSet(viewsets.ModelViewSet):
    queryset = Tips.objects.filter(insurance_type="auto")
    serializer_class = TipsSerializer

class LifeTipsViewSet(viewsets.ModelViewSet):
    queryset = Tips.objects.filter(insurance_type="life")
    serializer_class = TipsSerializer

class HealthTipsViewSet(viewsets.ModelViewSet):
    queryset = Tips.objects.filter(insurance_type="health")
    serializer_class = TipsSerializer

