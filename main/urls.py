from django.urls import path
from .views import Home, Results, error_404_views
urlpatterns = [
    path('', Home, name='home'),
    path('', Results, name='results'),
]

handler404 = error_404_views
