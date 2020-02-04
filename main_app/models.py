from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Debt(models.Model):
    debt = models.IntegerField()
    
    def __str__(self):
        return str(self.debt)

class Payment(models.Model):
    when = models.DateField(null = False)
    how_much = models.IntegerField()

    def __str__(self):
        return str(self.how_much)
