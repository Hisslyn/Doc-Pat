from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm 
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Doctor, TimeSlot
from django.urls import reverse



def doctor_registration(request):
    return HttpResponse("This is the doctor registration page. Congratulations on registering!")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a new URL:
            return redirect('doctor_registration_page')  # Adjust the redirect as needed
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def list_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'accounts/doctor_list.html', {'doctors': doctors})

def doctor_detail(request, doctor_id):
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    all_slots = TimeSlot.objects.all()
    return render(request, 'accounts/doctor_detail.html', {'doctor': doctor, 'all_slots': all_slots})

@login_required
def book_time_slot(request, doctor_id):
    if request.method == 'POST':
        doctor = get_object_or_404(Doctor, id=doctor_id)
        selected_slot_id = request.POST.get('slot_id')
        selected_slot = get_object_or_404(TimeSlot, id=selected_slot_id)

        if selected_slot.is_available:
            selected_slot.is_available = False
            selected_slot.user = request.user
            selected_slot.save()
            doctor.available_slots.remove(selected_slot)

            return redirect(reverse('booking_success'))
        else:
            return redirect(reverse('booking_error'))
    # If method is not POST, redirect to doctor's detail page or somewhere relevant.
    return redirect(reverse('doctor_detail', args=[doctor_id]))

def booking_success_view(request):
    # Logic for a successful booking, if any, goes here
    return render(request, 'booking_success.html')

def booking_error(request):
    # Logic for handling booking errors, if any, goes here
    return render(request, 'booking_error.html')

def home_view(request):
    # Your logic here
    return render(request, 'home.html')