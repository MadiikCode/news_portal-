from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация прошла успешно! Теперь можно читать новости.')
            return redirect('news_list')  # ← ВОТ ЭТА СТРОКА
    else:
        form = RegisterForm()
    return render(request, 'users/register.html', {'form': form})

