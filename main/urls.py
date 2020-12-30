from django.urls import path
from .views import Home, Results
urlpatterns = [
    path('', Home, name='home'),
    path('', Results, name='results'),



]
