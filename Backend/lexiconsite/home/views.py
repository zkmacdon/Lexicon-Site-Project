from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Home
class HomeView(TemplateView):
    model = Home
    context_object_name = 'home'
    template_name = 'home/index.html'
    

    
# Create your views here.
def index(request):
        return render(request, 'home/index.html')