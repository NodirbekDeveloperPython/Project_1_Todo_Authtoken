from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Plan(models.Model):
    nom = models.CharField(max_length=50)
    status = models.CharField(max_length=100)
    batafsil = models.TextField(blank=True)
    vaqt = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self): return self.nom