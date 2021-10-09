from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('', views.home, name='home'),

    # auth urls
    path('signup/', views.register_new_user, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('admin/', admin.site.urls),

    path('delete/<str:ext>', views.delete_url, name='deleteUrl'),
    path('<str:uid>/', views.redirect_to_url, name='redirect'),
]

