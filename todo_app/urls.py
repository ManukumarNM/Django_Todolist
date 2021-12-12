from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/<str:pk>',views.delete_view, name='delete'),
]
