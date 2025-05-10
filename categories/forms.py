# categories/forms.py
from django import forms
from django.utils.text import slugify
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'slug', 'description', 'image']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }

    # Метод для автоматического заполнения slug, если он пустой
    def clean_slug(self):
        slug = self.cleaned_data.get('slug')
        if not slug:
            slug = slugify(self.cleaned_data['name'])  # Генерация из name
        return slug