from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('action/<list_id>', views.action, name='action'),
    path('edit/<list_id>', views.edit_item, name='edit'),
]
