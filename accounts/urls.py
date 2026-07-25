from django.urls import path
from .views import RegisterView, LoginView, MyProfileView, FollowUserView, UnfollowUserView, LogoutView, ProfileView

urlpatterns = [
  path('register/', RegisterView.as_view()),
  path('login/', LoginView.as_view()),
  path('logout/',LogoutView.as_view()),
  path('profile/',MyProfileView.as_view() ),
  path('profile/<int:user_id>/', ProfileView.as_view(), name='profile'),
  path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
  path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
]