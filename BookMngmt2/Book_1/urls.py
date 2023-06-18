from django.urls import path
from . import views

urlpatterns = [
    path('modelform/', views.Search, name='form_method'),
    path('', views.Search, name='form_method'),
    
]
