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
    rating = Restaurant.objects.all()
    reviews = Review.objects.all()
    context = {
        'restaurants': restaurants,
        'location' : location,
        'rating' : rating,
        'reviews' : reviews
        }
    return render(request, 'restaurant_detail.html', context)


def restaurant_review(request):
    rating = Restaurant.objects.all()
    reviews = Review.objects.all()
    context = {
        'rating' : rating,
        'reviews' : reviews
    }
    return render(request, 'restaurant_review.html', context)

# class Menu(models.Model):
#     id = models.AutoField(primary_key=True)
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     menu_name = models.CharField(max_length=150)
#     created_at = models.DateField(default=timezone.now)
#     rating = models.FloatField(default=0, blank=True)
    
#     def __str__(self):
#         return self.menu_name
    
#     @staticmethod
#     def calculate_average_rating():
#         average_rating = Menu.objects.aggregate(Avg('rating')) ['rating_avg']
#         if average_rating is not None:
#             average_rating = round(average_rating, 2)
#         return average_rating

# class Review(models.Model):
#     id = models.AutoField(primary_key=True)
#     menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
#     review_text = models.TextField()
#     created_at = models.DateTimeField(default=timezone.now)