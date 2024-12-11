from rest_framework import serializers
from .models import Computer

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = '__all__'  # Include all fields in the response
