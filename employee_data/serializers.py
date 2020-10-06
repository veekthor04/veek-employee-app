from rest_framework import serializers
from .models import Data

class DataSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'firstName', 'lastName', 'employeeId', 'city',)
        model = Data