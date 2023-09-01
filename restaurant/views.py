from django.shortcuts import render, redirect
from .models import Restaurant, Menu, Review
from django.utils import timezone
from restaurant.forms import RatingForm
from django.urls import reverse

def home(request):
    # restaurants = Restaurant.objects.get(id=restaurant_id)
    today = timezone.now().date()
    restaurant_name = Restaurant.objects.all()
    menu = Menu.objects.filter(date=today)
    context = {
        # 'restaurants': restaurants,
        'restaurant_name' : restaurant_name,
        'menus' : menu
    }
    return render(request, 'home.html', context)


def restaurant_detail(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    # rating = Review.objects.get(restaurant=restaurants)
    reviews = Review.objects.filter(restaurant=restaurant).order_by('-created_at')
    
    for review in reviews:          # 이 부분 추가
        review.stars = '⭐' * int(review.rating)

    context = {
        'restaurant': restaurant,
        'reviews' : reviews,
        }
    return render(request, 'restaurant_detail.html', context)


def restaurant_review(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.save()

            return redirect('restaurant:restaurant_detail', restaurant_id=restaurant_id)

    else:
        form = RatingForm()

    reviews = Review.objects.all()
    context = {
        'restaurant': restaurant,
        'reviews': reviews,
        'form': form,
    }
    return render(request, 'restaurant_review.html', context)



# def restaurant_review(request, restaurant_id):
#     if request.method == 'POST':
#         form = RatingForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('restaurant_detail', restaurant_id)
#     else:
#         form = RatingForm()

#     rating = Restaurant.objects.all()
    
#     reviews = Review.objects.all()
#     context = {
#         'rating': rating,
#         'reviews': reviews,
#         'form': form,
#     }
#     return render(request, 'restaurant_review.html', context)
