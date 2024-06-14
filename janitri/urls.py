from django.urls import path
from .views import register_user, login_user, manage_patients, heart_rate_data, get_patient_details, get_patient_heart_rate

urlpatterns = [
    path('register', register_user, name='register_user'),
    path('login', login_user, name='login_user'),
    path('patients', manage_patients, name='manage_patients'),
    path('patients/<int:patient_id>',
         get_patient_details, name='get_patient_details'),
    path('patients/<int:patient_id>/heart-rate',
         get_patient_heart_rate, name='get_patient_heart_rate'),
    path('heart-rate', heart_rate_data, name='heart_rate_data'),
]
