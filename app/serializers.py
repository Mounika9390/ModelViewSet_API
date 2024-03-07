from rest_framework import serializers
from app.serializers import *
from app.models import *
class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'