# news/forms.py

from django import forms
from .models import News

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'published_date', 'author', 'image', 'is_published', 'category']
        widgets = {
            'published_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }


