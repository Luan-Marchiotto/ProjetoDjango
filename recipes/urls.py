from django.urls import path
from recipes.views import home
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home),
]