from django.urls import path
from users.views import SignInView, UserUpdateView, UsersListView, CurrentUserView

urlpatterns = [
    path('auth/admin/', SignInView.as_view()),
    path('users/', UsersListView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserUpdateView.as_view()),
]

