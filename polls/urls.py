from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PollViewSet, VoteViewSet, api_root, OptionViewSet

router = DefaultRouter()
router.register(r'polls', PollViewSet, basename='polls')
router.register(r"options", OptionViewSet, basename="vote")
router.register(r'votes', VoteViewSet, basename='votes')

urlpatterns = [
    # API root index
    path("", api_root, name="api-root"),

    # Router-generated endpoints
    path("", include(router.urls)),
]
