from django.urls import path
from .views import UserLoginView, UserLogoutView, UserProfileView, generate_report

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('generate-report/', generate_report, name='generate_report'),
]
