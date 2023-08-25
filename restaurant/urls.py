from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.home),
#    path('rest/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),

]
