from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255) 
    price = models.IntegerField()             
    description = models.TextField()
    shade_name = models.CharField(max_length=255,  default='Uncategorized')
    stock_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.name