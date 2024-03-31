from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list, name='board_list'),
    path('<int:board_id>/', views.board_detail, name='board_detail'),
    path('create/', views.board_create, name='board_create'),
]