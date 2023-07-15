from django.urls import path
from . import views


urlpatterns = [
    path('profile/<int:pk>/', views.profile, name='profile'),
    path('account/', views.account, name='account'),  
    path('update/', views.updateprofile, name='update'),
    path('delete/', views.delete, name='delete'),

]