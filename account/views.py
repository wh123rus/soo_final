from django.shortcuts import redirect, render
from restaurant.models import Restaurant, Menu, SuggestionBoard
from .forms import MenuForm

# Create your views here.
def restaurant_account(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            restaurant_name=form.cleaned_data['restaurant']
            form.save()
            return redirect('account:restaurant_account')
    else:
        form = MenuForm()
        
    return render(request, 'account/restaurant_account.html', {'form': form})


def home(request):
    return render(request, 'base.html')
