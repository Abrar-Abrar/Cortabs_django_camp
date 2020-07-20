from django.db import models
from django.urls import reverse
from datetime import date
# Create your models here.


class Product(models.Model):
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=250, blank=True,  null=True)
    price = models.PositiveIntegerField()
    create_at = models.DateField(default=date.today())

    def get_absolute_url(self):
        return reverse("product_details", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
