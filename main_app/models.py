from datetime import date
from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

# Create your models here.

MEALS = (
    ('B1', '1ˢᵗ Breakfast'),
    ('B2', '2ⁿᵈ Breakfast'),
    ('L1', '1ˢᵗ Lunch'),
    ('L2', '2ⁿᵈ Lunch'),
    ('D1', '1ˢᵗ Dinner'),
    ('D2', '2ⁿᵈ Dinner')
)


class Toy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self) -> str:
        return reverse("finches:toy_details", kwargs={'pk':self.pk})
    


class Finch(models.Model):
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=100)
    description = models.TextField()
    age = models.IntegerField(
        validators=[MinValueValidator(0, "Eggs don't count as finches yet")])
    toys = models.ManyToManyField(Toy)

    def __str__(self) -> str:
        return f"{self.id}: {self.name}, {self.breed}"

    def get_absolute_url(self) -> str:
        return reverse("finches:detail", kwargs={"id": self.id})

    def is_full(self) -> bool:
        return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=2,
                            choices=MEALS,
                            default=MEALS[0][0])
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ('-date',)
        
class Photo(models.Model):
    url = models.CharField(max_length=200)
    finch = models.ForeignKey(Finch,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Photo for finch id:{self.finch.id} @{self.url}"