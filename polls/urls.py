from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PollViewSet, VoteViewSet

router = DefaultRouter()
router.register(r'polls', PollViewSet, basename='polls')
router.register(r'votes', VoteViewSet, basename='votes')

urlpatterns = [
    path('', include(router.urls)),
]
