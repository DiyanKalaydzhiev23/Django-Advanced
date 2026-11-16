from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=120)
    country = models.CharField(max_length=80)
    founded_year = models.PositiveIntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=120)
    year = models.PositiveIntegerField()
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
    )
    color = models.CharField(max_length=40, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.model} ({self.year})"
