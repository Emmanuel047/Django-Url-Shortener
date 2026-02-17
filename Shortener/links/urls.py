from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    #path('create/', views.create_short, name='create'),
    #path('<str:short_code>/', views.redirect_url, name='redirect'),
    #path('<str:short_code>/stats/', views.stats, name='stats'),
]
