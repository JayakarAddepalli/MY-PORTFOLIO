from django.urls import path
from .views import *

app_name = 'APP'

urlpatterns = [
    path('', Home, name='home')
]