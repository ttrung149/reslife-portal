from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import StaffUpdateForm
from .models import Staff

# Create your views here.


def profile(request):
    staff_profile = Staff.objects.get(user=request.user)
    context = {
        'staff_profile': staff_profile
    }

    return render(request, 'staffs/profile.html', context)


def update_profile(request):
    if request.method == 'POST':
        form = StaffUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
            return redirect('profile')

    else:
        form = StaffUpdateForm(instance=request.user)

    context = {
        'form': form
    }

    return render(request, 'staffs/update_profile.html', context)
