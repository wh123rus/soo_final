from django.shortcuts import render

# def home(request):
#     # Your view logic here
#     return render(request, 'restaurant_app/index.html')

def home(request):
    return render(request, 'home.html')