from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudyGroupViewSet, StudyGroupMembershipViewSet, GroupMessageViewSet

router = DefaultRouter()
router.register('groups', StudyGroupViewSet, basename='groups')
router.register('memberships', StudyGroupMembershipViewSet, basename='memberships')
router.register('messages', GroupMessageViewSet, basename='messages')

urlpatterns = [
    path('', include(router.urls)),
]
