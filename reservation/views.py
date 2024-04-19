from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation
from .forms import ReserveTableForm

# Create your views here.


def reserve_table(request):
    if request.method == 'POST':
        form = ReserveTableForm(request.POST)
        if form.is_valid():
            reservation = form.save()
            return redirect('reservation_success', reservation_id=reservation.id)
    else:
        form = ReserveTableForm()
    return render(request, 'reservation.html', {'form': form})

def reservation_success(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'reservation_success.html', {'reservation': reservation})

def edit_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    if request.method == 'POST':
        form = ReserveTableForm(request.POST, instance=reservation)
        if form.is_valid():
            edited_reservation = form.save()
            return redirect('edit_success', reservation_id=edited_reservation.id)
    else:
        form = ReserveTableForm(instance=reservation)
    return render(request, 'edit_reservation.html', {'form': form})

def edit_success(request, reservation_id):
    edited_reservation = get_object_or_404(Reservation, id=reservation_id)
    return render(request, 'edit_success.html', {'edited_reservation': edited_reservation})
