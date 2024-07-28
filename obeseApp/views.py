from rest_framework import viewsets
from .models import MyFormData
from .serializers import MyFormDataSerializer 


class MyFormDataViewSet(viewsets.ModelViewSet):
    queryset = MyFormData.objects.all()
    serializer_class = MyFormDataSerializer
