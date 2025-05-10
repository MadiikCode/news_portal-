from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Category
from .forms import CategoryForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)  # FILES нужен для загрузки изображений
        if form.is_valid():  # Проверка валидности
            form.save()
            return redirect('category_list')  # Перенаправляем после успеха
    else:
        form = CategoryForm()  # Пустая форма для GET-запроса

    return render(request, 'categories/category_form.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'categories/category_list.html', {'categories': categories})


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    news_in_category = category.news.all()  # работает, потому что related_name='news'

    return render(request, 'categories/category_detail.html', {
        'category': category,
        'news': news_in_category,
    })

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('category_list')