from django.db import models
from django.contrib.auth.models import User
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator  # Import validator

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField()
    shade_name = models.CharField(max_length=100)
    stock_quantity = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product/', blank=True, null=True)
    image_url = models.URLField(max_length=200, default='http://example.com/default_image.jpg')

    def __str__(self):
        return self.name