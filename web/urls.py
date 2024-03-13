from django.contrib import admin
from django.urls import path

from web.views import book_add_view, main_view, registration_view, auth_view

urlpatterns = [
    path("auth/", auth_view, name="auth"),
    path('sign-in/', registration_view, name="sign"),
    path('book/add/', book_add_view, name="add"),
    path('', main_view, name="main"),
]
