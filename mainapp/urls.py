from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<str:ext>', views.delete_url, name='deleteUrl'),
    path('<str:uid>/', views.redirect_to_url, name='redirect'),
]

