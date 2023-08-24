from django.urls import path
from django.contrib.auth import views as auth_views
from common import views

app_name = 'common'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='common/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('register/done/', views.done, name='done'),
    path('logout/', auth_views.LogoutView.as_view(template_name='common/logout.html'), name='logout'),
    path('password_change/', views.password_change, name='password_change'),
    path('password_change/done/', views.password_change_done, name='password_change_done'),
]