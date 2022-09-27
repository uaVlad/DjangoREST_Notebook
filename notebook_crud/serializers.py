from rest_framework import serializers
from .models import UserFields, FullUserAddress


class UserFieldsCreateAPIViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserFields
        fields = "__all__"


class FullUserAddressAPIViewSerializers(serializers.ModelSerializer):
    class Meta:
        model = FullUserAddress
        fields = "__all__"
