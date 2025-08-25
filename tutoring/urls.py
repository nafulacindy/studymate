from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TutoringSessionViewSet

router = DefaultRouter()
router.register('sessions', TutoringSessionViewSet, basename='session')

urlpatterns = [
    path('', include(router.urls)),
]
