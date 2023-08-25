from django.shortcuts import render
from .models import Restaurant, Menu, Review, SuggestionBoard
from django.utils import timezone

# def home(request):
#     # Your view logic here
#     return render(request, 'restaurant_app/index.html')

# def home(request):
#     today = timezone.now().date()
#     today_menu = Menu.objects.filter(created_at__date=today)
#     return render(request, 'home.html', {'today_menu':today_menu})

# def home(request):
#     today = timezone.now().date()
#     menus = Menu.objects.filter(created_at__date=today).select_related('restaurant', 'menu_name')
#     return render(request, 'home.html', {'menus': menus})
    
def home(request):
    today = timezone.now().date()
    restaurant_name = Restaurant.objects.order_by()
    menu = Menu.objects.filter(created_at=today)
    context = {
        'restaurant_name' : restaurant_name,
        'menu' : menu
    }
    return render(request, 'home.html', context)

# def restaurant_detail(request, restaurant_id):
#     restaurant_list = Restaurant.objects.get(id=restaurant_id)
#     context = {'restaurant_list':restaurant_list}
#     return render(request, 'rest/restaurant_list.html', context)
    

# def index(request):
#     restaurant_list = Restaurant.objects.order_by('restaurant_name')
#     context = {'restaurant_list': restaurant_list}
#     return render(request, 'rest/restaurant_list.html', context)

# def detail(request, restaurant_id):
#     restaurant = Restaurant.objects.get(id=restaurant_id)
#     context = {'restaurant': restaurant}
#     return render(request, 'rest/restaurant_detail.html', context)
