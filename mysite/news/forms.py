from django import forms
from django.db import models
from django.forms import fields, widgets
from .models import Category
from .models import News
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ContactForm(forms.Form):
    subject = forms.CharField(label="Тема:",widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label="Тема:",widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="Имя пользователя:",widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(label="Email:",widget=forms.EmailInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Пароль:",widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Подтверждения пароля:",widget=forms.PasswordInput(attrs={"class": "form-control"}))


    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']
        widgets = {
            'USERNAME': forms.TextInput(attrs={"class": "form-control"}),
            'content':forms.Textarea(attrs={"class": "form-control","rows":5}), 
            'category': forms.Select(attrs={"class": "form-control"}),
        }

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label="Имя пользователя:",widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label="Пароль:",widget=forms.PasswordInput(attrs={"class": "form-control"}))

    
    class Meta:
        model = User

class NewsForm2(forms.Form):
    title = forms.CharField(max_length=150,label="Название", widget=forms.TextInput(attrs={"class": "form-control"}))
    content = forms.CharField(label="Текст", required=False, widget=forms.Textarea(attrs={"class": "form-control","rows":5}))
    is_published = forms.BooleanField(label="Опубликовано?", initial=True)
    category = forms.ModelChoiceField(empty_label="Выберите категорию", queryset=Category.objects.all(),label="Категория", widget=forms.Select(attrs={"class": "form-control"}))

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        #fields = '__all__' 
        fields = ['title', 'content','is_published','category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'content':forms.Textarea(attrs={"class": "form-control","rows":5}), 
            'category': forms.Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError("Название не должно начинаться с цифры")
        return title
