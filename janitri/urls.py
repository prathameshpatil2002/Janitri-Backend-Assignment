from django.urls import path
from .views import register_user, login_user, manage_patients, heart_rate_data

urlpatterns = [
    path('register/', register_user, name='register_user'),
    path('login/', login_user, name='login_user'),
    path('patients/', manage_patients, name='manage_patients'),
    path('heart-rate/', heart_rate_data, name='heart_rate_data'),
]
