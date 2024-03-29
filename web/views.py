from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
from web.forms import AddBookForm, RegisterForm, AuthForm

from django.contrib.auth import get_user_model, authenticate, login, logout

from web.models import Book

User = get_user_model()


def main_view(request):
    book = Book.objects.all()
    return render(request, "web/main.html", {
        "books": book
    })


def registration_view(request):
    form = RegisterForm()
    is_success = False
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data['username'],
                        email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            print(form.cleaned_data)
            is_success = True
    return render(request, "web/registration.html", {
        "form": form,
        "is_success": is_success
    })


def auth_view(request):
    form = AuthForm()
    if request.method == "POST":
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, "Invalid user")
            else:
                login(request, user)
                return redirect("main")
    return render(request, "web/auth.html", {"form": form})


def book_add_view(request):
    form = AddBookForm()
    if request.method == 'POST':
        form = AddBookForm(data=request.POST, initial={"user": request.user})
        if form.is_valid():
            form.save()
            return redirect('main')
    return render(request, "web/book_add.html", {'form': form})


def logout_view(request):
    logout(request)
    return redirect("main")