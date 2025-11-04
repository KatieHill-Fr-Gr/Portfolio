from django.urls import path
from users.views import SignInView, UserUpdateView, UsersListView

urlpatterns = [
    path('auth/admin/', SignInView.as_view()),
    path('users/', UsersListView.as_view(), name='users-list'),
    path('users/me/', CurrentUserView.as_view(), name='current-user'),
    path('users/<int:pk>/', UserUpdateView.as_view()),
]

