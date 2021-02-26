from django.urls import path

from .views import Results

urlpatterns = [
    path('', Results, name='results'),

]
