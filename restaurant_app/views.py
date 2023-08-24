from django.shortcuts import render

def index(request):
    # Your view logic here
    return render(request, 'restaurant_app/index.html')