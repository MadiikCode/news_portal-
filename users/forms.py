from django import forms
from .models import User  # Изменяем импорт


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput(), label='Подтверждение пароля')

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_password2(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

class UserSignForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']