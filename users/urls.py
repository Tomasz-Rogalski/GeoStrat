from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name = 'register'),
    path('logged_out/', views.logged_out, name = 'logged_out'),
    path('user_account/', views.user_account, name='user_account'),
    path('view_account/(<str:username>)/', views.view_account, name='view_account'),
]
    
