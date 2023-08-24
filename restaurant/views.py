from django.shortcuts import render
from .models import Restaurant, Menu
from django.utils import timezone

# def home(request):
#     # Your view logic here
#     return render(request, 'restaurant_app/index.html')

def home(request):
    today = timezone.now().date()
    today_menu = Menu.objects.filter(created_at__date=today)
    return render(request, 'home.html', {'today_menu':today_menu})