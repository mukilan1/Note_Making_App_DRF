from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, CreateUserView
from rest_framework_simplejwt.views import  TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('Notes',NoteViewSet,basename='Notes',)

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('verify/', TokenVerifyView.as_view(), name='verify'),
    path('',include(router.urls))
]
