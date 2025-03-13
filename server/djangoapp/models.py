# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    country_of_origin = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    name = models.CharField(max_length=100)

    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('CONVERTIBLE', 'Convertible'),
        ('HATCHBACK', 'Hatchback'),
        ('PICKUP', 'Pickup Truck'),
        ('MINIVAN', 'Minivan'),
        ('SPORTSCAR', 'Sports Car'),
        ('CROSSOVER', 'Crossover'),
        ('MUSCLE', 'Muscle Car'),
        ('ELECTRIC', 'Electric'),
        ('HYBRID', 'Hybrid'),
    ]

    type = models.CharField(max_length=20, choices=CAR_TYPES, default='SUV')

    year = models.IntegerField(
        default=2025,
        validators=[
            MaxValueValidator(2025),
            MinValueValidator(2015)
        ]
    )

    engine_type = models.CharField(max_length=50, blank=True, null=True)
    horsepower = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.car_make.name} {self.name}'
