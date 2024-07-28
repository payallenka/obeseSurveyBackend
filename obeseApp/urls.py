from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MyFormDataViewSet

router = DefaultRouter()
router.register(r'api/formdata', MyFormDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
