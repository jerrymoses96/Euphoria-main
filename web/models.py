from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser





class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='category/images', null=True, blank=True)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.name


class Gender(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='product/images', null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    ratings = models.PositiveIntegerField()
    comment_count = models.PositiveIntegerField()
    description = models.TextField()
    sizes = models.ManyToManyField(Size)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)  # New field

    def __str__(self):
        return self.name


class Wishlist(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="User")

    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} - {self.product.name}"


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, related_name="customuser")
   
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Added quantity field

    class Meta:
        # Ensure each product is unique per user
        unique_together = ('user', 'product')

    def __str__(self):
        return f"{self.user.username}'s cart - {self.product.name} (x{self.quantity})"
