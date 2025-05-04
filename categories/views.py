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
    return render(request, 'categories/category_detail.html', {'category': category})

def category_add(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'categories/category_add.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('news_list')