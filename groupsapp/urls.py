from rest_framework.routers import DefaultRouter
from .views import StudyGroupViewSet, GroupMessageViewSet

router = DefaultRouter()
router.register(r'groups', StudyGroupViewSet)
router.register(r'messages', GroupMessageViewSet)

urlpatterns = router.urls
