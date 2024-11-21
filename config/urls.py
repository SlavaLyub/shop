from django.contrib import admin
from django.urls import path, include

from shop import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),
]
