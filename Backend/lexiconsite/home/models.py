from django.db import models
from django.urls import reverse
# Create your models here.
class Home(models.Model):
    def get_absolute_list_url(self):
        return reverse('home:index')