from django.urls import path, include
from .views import UserViewSet, RegisterViewSet, LoginViewSet, LogoutViewSet

urlpatterns = [
    path("register/", RegisterViewSet.as_view(), name="register"),
    path("login/", LoginViewSet.as_view(), name="login"),
    path("logout/", LogoutViewSet.as_view(), name="logout"),
]