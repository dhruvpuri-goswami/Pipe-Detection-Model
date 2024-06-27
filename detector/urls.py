from django.urls import path
from .views import detect_pipes

urlpatterns = [
    path('detect/', detect_pipes, name='detect-pipes'),
]