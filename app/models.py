from django.db import models


class Category(models.Model):
    title = models.CharField()

    def __str__(self):
        return self.title


class Product(models.Model):
    image = models.ImageField(null=True, blank=True)
    rating = models.FloatField(default=1)
    title = models.CharField()
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    category = models.ForeignKey(to='app.Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title






