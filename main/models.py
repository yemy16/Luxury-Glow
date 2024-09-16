import uuid
from django.db import models

class LuxuryGlow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    description = models.TextField()
    image = models.ImageField()
    shade_name = models.CharField(max_length=100)
    stock_quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.name