from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('common/', include("common.urls")),
    path('restaurant/', include("restaurant_app.urls")),
]
