from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('article/<str:slug>', views.detail_list, name='detail_list'),
    path('create/', views.createpost, name='createpost'),
    path('update/<int:pk>/', views.updatepost, name='updatepost')

]