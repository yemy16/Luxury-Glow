from django.db import models

class LuxuryGlam(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()
    image = models.ImageField()
    shade_name = models.CharField(max_length=100)
    stock_quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.name