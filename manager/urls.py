from django.urls import path
from .views import reservations, update_reservation

app_name = 'manager'

urlpatterns = [
    path('reservations/', reservations, name='reservations'),
    path('reservations/update/<int:pk>/', update_reservation, name='update_reservation'),
]
