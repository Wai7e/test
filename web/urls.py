from django.contrib import admin
from django.urls import path

from web.views import book_add_view, main_view

urlpatterns = [
    path('book/add/', book_add_view),
    path('', main_view),
]
