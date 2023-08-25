from django.contrib import admin
from restaurant.models import Restaurant, Menu, Food, Review, SuggestionBoard
#from django.contrib.auth.models import User

#admin.site.register(User)
#admin.site.register(User)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Food)
admin.site.register(Review)
admin.site.register(SuggestionBoard)