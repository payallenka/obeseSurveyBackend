from rest_framework import serializers
from .models import MyFormData

class MyFormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyFormData
        fields = '__all__'
