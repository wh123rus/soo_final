from django.shortcuts import render
from .models import Restaurant, Menu, Review, SuggestionBoard
from django.utils import timezone

def home(request):
    today = timezone.now().date()
    restaurant_name = Restaurant.objects.all()
    menu = Menu.objects.filter(created_at=today)
    context = {
        'restaurant_name' : restaurant_name,
        'menus' : menu
    }
    return render(request, 'home.html', context)

# def menu_detail(request):
#     restaurant_name =  Restaurant.objects.order_by()
#     food = Food.objects.all()
#     review = Review.objects.order_by('-created_at')
#     context = {
#         'restaurant_name' : restaurant_name,
#         'food' : food,
#         'review' : review,        
#     }
#     return render(request, 'menu_detail.html', context)
