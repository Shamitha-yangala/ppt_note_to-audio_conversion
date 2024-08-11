from django.urls import path
from . import views

urlpatterns = [
   path('', views.ppt_file_upload, name='ppt_file_upload'),
]