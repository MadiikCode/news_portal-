from django.db import models
from django.utils import timezone
from django.urls import reverse
from categories.models import Category


class News(models.Model):
    title = models.CharField( max_length=100, verbose_name='Заголовок',default='Без названия')
    content = models.TextField(verbose_name='Содержание')
    published_date = models.DateTimeField(verbose_name='Дата публикации',default=timezone.now ) # Используем timezone.now вместо auto_now_add для гибкости)
    author = models.CharField( max_length=100,verbose_name='Автор', default='Администратор' )
    image = models.ImageField(upload_to='news_images/',verbose_name='Изображение',null=True, blank=True )
    created_at = models.DateTimeField( verbose_name='Дата создания' ,auto_now_add=True )
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='news',verbose_name='Категория')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_date']

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('news_detail2', kwargs={'pk': self.pk})

