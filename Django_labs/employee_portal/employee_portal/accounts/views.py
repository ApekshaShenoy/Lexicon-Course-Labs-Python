# accounts/views.py
from django.shortcuts import render, redirect
from .forms import EmployeeRegistrationForm, EmployeeProfileForm
from django.contrib import messages
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        user_form = EmployeeRegistrationForm(request.POST)
        profile_form = EmployeeProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Welcome! Your employee account has been created.')
            return redirect('profile_preview', user_id=user.id)
    else:
        user_form = EmployeeRegistrationForm()
        profile_form = EmployeeProfileForm()

    return render(request, 'accounts/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def profile_preview(request, user_id):
    user = User.objects.get(id=user_id)
    profile = getattr(user, 'employeeprofile', None)
    return render(request, 'accounts/profile_preview.html', {
        'user': user,
        'profile': profile
    })
