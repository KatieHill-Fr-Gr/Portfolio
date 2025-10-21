from django.urls import path
from users.views import SignInView, UserUpdateView

urlpatterns = [
    path('api/auth/admin/', SignInView.as_view()),
    path('<int:pk>/', UserUpdateView.as_view())
]

