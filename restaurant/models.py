from django.db import models
from django.db.models import Avg
from django.utils import timezone


class Restaurant(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant_name = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    event = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.restaurant_name

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, default='')
    menu_name = models.CharField(max_length=150)
    date = models.DateField(default=timezone.now)
    

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    review_text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    rating = models.FloatField(default=0, blank=True)
    
    def __str__(self):
        return f"Review for {self.restaurant.restaurant_name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class SuggestionBoard(models.Model):
    id = models.AutoField(primary_key=True)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    post_content = models.TextField()
