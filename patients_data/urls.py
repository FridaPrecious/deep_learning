from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('patients/add/', views.patient_create, name='patient_create'),
    path('patients/edit/<int:patient_id>/', views.patient_update, name='patient_update'),
    path('patients/delete/<int:patient_id>/', views.patient_delete, name='patient_delete'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]
