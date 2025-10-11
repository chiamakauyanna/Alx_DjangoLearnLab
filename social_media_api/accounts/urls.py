from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterView, LoginView, ProfileView, UserViewSet, create_admin

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    # Temporary admin creation route
    path("create-admin/", create_admin),

    # Auth and profile routes
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),

    # Follow/unfollow routes
    path('follow/<int:user_id>/', UserViewSet.as_view({'post': 'follow'}), name='follow_user'),
    path('unfollow/<int:user_id>/', UserViewSet.as_view({'post': 'unfollow'}), name='unfollow_user'),

    # Router URLs
    path('', include(router.urls)),
]
