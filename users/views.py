from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate, login, logout
)
from .forms import UserRegisterForm, UserSignForm


def register_user_view(request):
    if request.method == 'POST':
        form_register_user = UserRegisterForm(request.POST)
        if form_register_user.is_valid():
            username = form_register_user.cleaned_data['username']
            email = form_register_user.cleaned_data['email']
            password = form_register_user.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                form_register_user.add_error('username', 'Пользователь с таким именем уже существует.')

            elif User.objects.filter(email=email).exists():
                form_register_user.add_error('email', 'Пользователь с таким email уже существует.')

            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password=password,
                )
                user.save()
                authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('news:news')

    else:
        form_register_user = UserRegisterForm()

    context = {'form_register_user': form_register_user}
    return render(request, 'users/register.html', context)


def sign_user_view(request):
    if request.method == 'POST':
        form_sign_user = UserSignForm(request.POST)
        if form_sign_user.is_valid():
            username = form_sign_user.cleaned_data['username']
            password = form_sign_user.cleaned_data['password']

            # Используем authenticate для проверки пользователя
            user = authenticate(request, username=username, password=password)

            if user is not None:
                # Пользователь найден, логиним
                login(request, user)
                return redirect('news:news')
            else:
                # Ошибка аутентификации, добавляем ошибку на форму
                form_sign_user.add_error('username', 'Неверное имя пользователя или пароль.')

    else:
        form_sign_user = UserSignForm()

    context = {'form_sign_user': form_sign_user}
    return render(request, 'users/sign.html', context)


def sign_out_user_view(request):
    logout(request)  # ✅ просто передаём request
    return redirect('news:news')  # или на главную после выхода