from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('login', vk_authorization),
    path('callback', vk_callback),
    path('get-json', json_file_data),
    path('users', json_data),
]
