from django.shortcuts import render,get_object_or_404
from .models import News, Category
from .forms import NewsForm
from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy



def news_list(request):
  #  news = News.objects.filter(is_published=True).order_by('-created_at')
   # print(f"Найдено новостей: {news.count()}")
  #  return render(request, 'news/news.html', {'news': news})
      news = News.objects.filter(is_published=True).order_by('-created_at')
      return render(request, 'news/news.html', {'news': news})




#
# def news_create(request, ):
#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('news_list')
#     else:
#         form = NewsForm()
#     return render(request, 'news/news_form.html', {'form': form})




class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news_detail'


# class NewsCreateView(LoginRequiredMixin, CreateView):
#     model = News
#     form_class = NewsForm
#     template_name = 'news_app/create.html'
#     success_url = reverse_lazy('news_app:news')

# def news_create_view(request, category_slug):
#     if request.method == 'POST':
#         form = NewsForm(request.POST, request.FILES)
#         if form.is_valid():
#             news = form.save(commit=False)
#             news.author = request.user.username
#             # можно здесь привязать категорию по slug:
#             # from .models import Category
#             # category = get_object_or_404(Category, slug=category_slug)
#             # news.category = category
#             news.save()
#             return redirect('news:news')
#     else:
#         form = NewsForm()
#     return render(request, 'news/create.html', {'form': form})
    # else:
    #     form = NewsForm()
    # return render(request, 'news/create.html', {'form': form})
'''
   #     if form.is_valid():
    #         title = form.cleaned_data['title']
    #         name = form.cleaned_data['name']
    #         content = form.cleaned_data['content']
    #         category = form.cleaned_data['category']
    #
    #         news = News.objects.create(
    #             title=title,
    #             name=name,
    #             content=content,
    #             category=category,
    #         )
    #         news.save()
    #         return redirect('news:news')
    # else:
    #     form = NewsForm()
    #
    # context = {
    #     'form': form,
    # }
    #
    # return render(request, 'news/create.html', context)
'''


def news_create_view(request, category_slug=None):
    # Если категория нужна, но не обязательна
    category = None
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)

    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            if category:
                news.category = category
            news.save()
            return redirect('news:news')
    else:
        form = NewsForm(initial={'category': category} if category else None)

    return render(request, 'news/create.html', {'form': form, 'category': category})

class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news/create.html'
    success_url = reverse_lazy('news:news')

    def form_valid(self, form):
        form.instance.author = self.request.user.username
        return super().form_valid(form)


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news/delete.html'
    context_object_name = 'new'
    success_url = reverse_lazy('news:news')


def news_delete_view(request, pk):
    new = News.objects.get(pk=pk)
    new.delete()
    return redirect('news:news')


from .models import Category
from .forms import CategoryForm


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('news:category_list')  # Редирект на список категорий
            except IntegrityError:
                form.add_error('slug', 'Категория с таким слагом уже существует.')
    else:
        form = CategoryForm()

    return render(request, 'news/add_category.html', {'form': form})

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'news/category_list.html', {'categories': categories})




def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    # Можно добавить дополнительную логику, например, для вывода новостей этой категории
    return render(request, 'news/category_detail.html', {'category': category})