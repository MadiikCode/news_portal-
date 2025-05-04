from django.db import models
from django.utils import timezone
from django.urls import reverse



class News(models.Model):
    title = models.CharField( max_length=100, verbose_name='Заголовок',default='Без названия')
    content = models.TextField(verbose_name='Содержание')
    published_date = models.DateTimeField(verbose_name='Дата публикации',default=timezone.now ) # Используем timezone.now вместо auto_now_add для гибкости)
    author = models.CharField( max_length=100,verbose_name='Автор', default='Администратор' )
    image = models.ImageField(upload_to='news_images/',verbose_name='Изображение',null=True, blank=True )
    created_at = models.DateTimeField( verbose_name='Дата создания' ,auto_now_add=True )
    is_published = models.BooleanField(default=True)


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_date']

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk': self.pk})

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Название категории'
    )
    slug = models.SlugField(
        max_length=100,
        unique=True,
        verbose_name='URL категории'
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name