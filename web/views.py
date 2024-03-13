from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


# Create your views here.


def main_view(request):
    year = datetime.now().year
    return render(request, "web/main.html", {
        "year": year
    })


def book_add_view(request):
    return request
