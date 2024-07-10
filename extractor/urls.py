from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_form, name='upload_form'),
    path('extract/', views.extract_data, name='extract_data'),
]
