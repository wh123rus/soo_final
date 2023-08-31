from django import forms
from .models import Review

class RatingForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating']
        widgets = {
            'rating': forms.RadioSelect(choices=[
                (5, '⭐⭐⭐⭐⭐'),
                (4, '⭐⭐⭐⭐'),
                (3, '⭐⭐⭐'),
                (2, '⭐⭐'),
                (1, '⭐'),
            ]),
            'review_text': forms.Textarea(attrs={'rows': 6, 'cols': 50, 'style': 'resize: none;'})
        }
