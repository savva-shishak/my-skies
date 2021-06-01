from . import views
from django.urls import path

urlpatterns = [
    path('numbers/', views.get_numbers_and_flights),
]
