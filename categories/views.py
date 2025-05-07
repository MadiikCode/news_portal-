from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from .models import Category
from .forms import CategoryForm
from django.contrib.auth import logout
from django.shortcuts import redirect


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