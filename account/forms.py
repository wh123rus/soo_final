from django import forms
from django.db import models
from restaurant.models import Menu 

class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu 
        fields = ['restaurant','date', 'menu_name']
        widgets = {
            'menu_name' : forms.Textarea(attrs={'rows': 6, 'cols': 20, 'style': 'resize: none;'})
        }
        
        
