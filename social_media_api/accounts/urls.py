from .views import RegisterView, LoginView, ProfileView, UserViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('follow/<int:user_id>/', UserViewSet.as_view({'post': 'follow'}), name='follow_user'),
    path('unfollow/<int:user_id>/', UserViewSet.as_view({'post': 'unfollow'}), name='unfollow_user'),
    path('', include(router.urls))
]
