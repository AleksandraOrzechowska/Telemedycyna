from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login_patient/', views.login_patient, name='login_patient'),
    path('login_doctor/', views.login_doctor, name='login_doctor'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('register/', views.register_user, name='register'),
    path('examinations/', views.examinations, name='examinations'),
    path('blood_tests/', views.blood_tests, name='blood_tests'),
    path('other_examinations/', views.other_examinations, name='other_examinations'),
]






