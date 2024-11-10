from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'blogs', BlogView, basename='blog')

urlpatterns = [
    path('', include(router.urls)),
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),

]