from django.contrib import admin
from django.urls import path

from web.views import book_add_view, main_view, registration_view

urlpatterns = [
    path('sign-in/', registration_view),
    path('book/add/', book_add_view),
    path('', main_view),
]
