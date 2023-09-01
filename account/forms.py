from django import forms
from django.db import models
from restaurant.models import Menu 

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu 
        fields = ['restaurant','date', 'menu_name']