from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('feedback/', views.feedback, name='feedback'),
    path('contact/', views.contact, name='contact'),
    path('record/', views.record, name='record'),
    path('save/audio', views.save_audio, name='save_audio'),
    path('predict/depression/<int:id>', views.predict_depression, name='predict_depression'),
]