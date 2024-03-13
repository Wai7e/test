from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
from web.forms import AddBookForm, RegisterForm
from web.models import Book
from django.contrib.auth import get_user_model

User = get_user_model()


def main_view(request):
    year = datetime.now().year
    return render(request, "web/main.html", {
        "year": year
    })


def registration_view(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['user_name'],
                        email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            print(form.cleaned_data)

    return render(request, "web/registration.html", {
        "form": form
    })


def auth_view(request):
    return render(request, "web/auth.html")


def book_add_view(request):
    form = AddBookForm()
    if request.method == 'POST':
        form = AddBookForm(data=request.POST)
        if form.is_valid():
            book = Book(title=form.cleaned_data["name"], author=form.cleaned_data["author"],
                        category=form.cleaned_data["category"])
            book.save()
    return render(request, "web/book_add.html", {'form': form})
