from django.shortcuts import render,get_object_or_404
from .models import News


def news_list(request):
    news = News.objects.filter(is_published=True).order_by('-created_at')
    print(f"Найдено новостей: {news.count()}")
    return render(request, 'news/news_list.html', {'news': news})



def news_detail2(request, pk):
    news = get_object_or_404(News, pk=pk, is_published=True)
    return render(request, 'news/news_detail.html', {'news': news})