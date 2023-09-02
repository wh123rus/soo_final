from django.urls import path
from . import views

app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name='home'),

    # 일주일치 메뉴
    path('menu', views.menu_list, name='menu_list'),

    # 식당 목록
    path('rest', views.restaurant_list, name='restaurant_list'),
    # 식당 세부 페이지
    path('rest/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    # 식당 리뷰 작성 페이지
    path('rest/review/<int:restaurant_id>/', views.restaurant_review, name='restaurant_review'),

]
