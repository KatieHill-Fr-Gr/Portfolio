from django.urls import path
from users.views import SignInView, UserUpdateView, UsersListView

urlpatterns = [
    path('auth/admin/', SignInView.as_view()),
    path('', UsersListView.as_view(), name='users-list'),
    path('<int:pk>/', UserUpdateView.as_view()),
]

