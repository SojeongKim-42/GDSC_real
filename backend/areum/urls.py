# plat

from django.urls import path

from . import views

urlpatterns = [
    path('', views.ListClass.as_view()),
    path('<int:pk>/', views.DetailClass.as_view()),
]
