from django.shortcuts import render,get_object_or_404
from .models import News
from .forms import NewsForm
from django.shortcuts import redirect




def news_list(request):
  #  news = News.objects.filter(is_published=True).order_by('-created_at')
   # print(f"Найдено новостей: {news.count()}")
  #  return render(request, 'news/news_list.html', {'news': news})
  news_list = News.objects.all()  # Получите все новости
  return render(request, 'news/news_list.html', {'news_list': news_list})


def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk, is_published=True)
    return render(request, 'news/news_detail.html', {'news': news})




def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/news_form.html', {'form': form})