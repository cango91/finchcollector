from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Finch(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField(validators=[MinValueValidator(0,"Eggs don't count as finches yet")])
    
    def __str__(self) -> str:
        return f"{self.id}: {self.name}, {self.breed}"