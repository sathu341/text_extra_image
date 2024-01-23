from django.urls import path

from .views import index, capture_image



urlpatterns = [
    path('', index, name='index'),
    path('capture/', capture_image, name='capture_image'),
]