from django.urls import path
from .views import HomeView

app_name = 'home'

urlpatterns = [
    # post views
    path('', HomeView.as_view(), name='index'),
]