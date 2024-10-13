from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('telemarket_data/', views.telemarket_data, name='telemarket_data'),
    path('success/', views.success, name='success'),
    


]
