from django.shortcuts import render, redirect ,get_object_or_404
from .models import Restaurant, Menu, Review
from django.utils import timezone
from restaurant.forms import RatingForm
from django.urls import reverse
from django.db.models import Avg

def home(request):
    today = timezone.now().date()
    restaurant_name = Restaurant.objects.all()
    menus = Menu.objects.filter(date=today)
    context = {
        'restaurant_name' : restaurant_name,
        'menus': menus,
    }
    return render(request, 'home.html', context)

def restaurant_list(request):
    restaurant = Restaurant.objects.all()
    context = {
        'restaurants': restaurant,
    }
    return render(request, 'rest/restaurant_list.html', context)

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, pk=restaurant_id)

    # 해당 레스토랑의 모든 리뷰 가져오기
    reviews = Review.objects.filter(restaurant=restaurant).order_by('-created_at')

    # 각 리뷰의 별점을 별표로 변환하여 'stars' 필드 추가
    for review in reviews:
        review.stars = '⭐' * int(review.rating)

    # 해당 레스토랑의 별점 평균 계산
    average_rating = Review.objects.filter(restaurant=restaurant).aggregate(Avg('rating'))['rating__avg']

    context = {
        'restaurant': restaurant,
        'reviews': reviews,
        'average_rating': average_rating,
    }

    return render(request, 'rest/restaurant_detail.html', context)


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
    return render(request, 'rest/restaurant_review.html', context)