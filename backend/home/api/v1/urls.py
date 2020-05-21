from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import CustomTextViewSet, R1ViewSet, R2ViewSet, HomePageViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
    HomePageViewSet,
    CustomTextViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("customtext", CustomTextViewSet)
router.register("homepage", HomePageViewSet)
router.register("r2", R2ViewSet)
router.register("r1", R1ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
