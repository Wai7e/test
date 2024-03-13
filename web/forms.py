from django import forms
from django.contrib.auth import get_user_model

from web.models import Book

User = get_user_model()


class AddBookForm(forms.ModelForm):
    title = forms.CharField(max_length=256)
    author = forms.CharField(max_length=256)
    category = forms.CharField(max_length=256)

    def save(self, commit=True):
        self.instance.user = self.initial['user']
        return super().save(commit)

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['title'] == cleaned_data['author'] == cleaned_data['category']:
            self.add_error("title", "все поля одинаковы!")
        return cleaned_data

    class Meta:
        model = Book
        fields = ('title', 'author', 'category')


class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            self.add_error("password", "password incorrect")
        return cleaned_data

    class Meta:
        model = User
        fields = ("email", 'username', "password", "password2")


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
