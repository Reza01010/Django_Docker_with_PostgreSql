from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(),name='home'),
    path('aboutus/', views.AboutUsPagesView.as_view(), name='aboutus'),
]