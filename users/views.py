from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignUpForm, UserProfileForm
from .models import User
import uuid


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Пользователь не активен до подтверждения
            user.verification_token = str(uuid.uuid4())
            user.save()

            # Отправка email с подтверждением
            subject = 'Подтвердите ваш email'
            message = f'Для подтверждения перейдите по ссылке: http://{request.get_host()}/verify-email/{user.verification_token}/'
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

            return redirect('verify_email')
    else:
        form = SignUpForm()
    return render(request, 'users/sign_up.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'users/user_profile.html', {'form': form})


def verify_email(request, token):
    try:
        user = User.objects.get(verification_token=token)
        user.is_active = True
        user.email_verified = True
        user.verification_token = None
        user.save()
        login(request, user)
        return redirect('profile')
    except User.DoesNotExist:
        return render(request, 'users/verify_email.html', {'success': False})

