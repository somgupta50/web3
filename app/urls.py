from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('feedback/', views.feedback, name='feedback'),
    path('contact/', views.contact, name='contact'),
]