from django.shortcuts import render, redirect, get_object_or_404
from .forms import CustomUserCreationForm  # Make sure to import the correct form
from django.http import HttpResponse
from .models import Doctor, TimeSlot

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