from django.urls import path, include
from .views import Results
urlpatterns = [
    path('', Results, name='results'),



]
