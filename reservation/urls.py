from django.urls import path
from . import views

urlpatterns = [
    path('reserve_table/', views.reserve_table, name='reserve_table'),
    path('reservation/<int:reservation_id>/success/', views.reservation_success, name='reservation_success'),
    path('reservation/<int:reservation_id>/edit/', views.edit_reservation, name='edit_reservation'),
    path('reservation/<int:reservation_id>/edit/success/', views.edit_success, name='edit_success'),
]
