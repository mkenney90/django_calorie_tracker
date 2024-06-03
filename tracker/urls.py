from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_entry, name='add_entry'),
    path('delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),
]
