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


def restaurant_detail(request, restaurant_id):
    restaurants = Restaurant.objects.get(id=restaurant_id)
    location = Restaurant.objects.all()
    event = Restaurant.objects.all()
    rating = Menu.objects.all()
    reviews = Review.objects.order_by('-created_at') # 이거 바꿈. 원래는 all()
    context = {
        'restaurants': restaurants,
        'location' : location,
        'event' : event,
        'reviews' : reviews,
        'rating' : rating
        }
    return render(request, 'restaurant_detail.html', context)

# class Review(models.Model):
#     id = models.AutoField(primary_key=True)
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
#     review_text = models.TextField()
#     created_at = models.DateTimeField(default=timezone.now)

def restaurant_review(request):
    rating = Restaurant.objects.all()
    reviews = Review.objects.all()
    context = {
        'rating' : rating,
        'reviews' : reviews
    }
    return render(request, 'restaurant_review.html', context)

