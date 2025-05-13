# news/forms.py

from django import forms
from .models import News, Category
from django import template



class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'published_date', 'author', 'image', 'is_published', 'category']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

register = template.Library()

@register.filter(name='add_class')
def add_class(value, css_class):
    return value.as_widget(attrs={'class': css_class})


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']