from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255, default="title")

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255, default="title")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default = 1)
    body = models.TextField()
    category = models.CharField(max_length=255, default="Mattress")
    condition = models.CharField(max_length=255, default="Good")
    brand = models.CharField(max_length=255, default="Brand")
    phone = PhoneNumberField(null=False, blank=False, default="+911111111111")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    email = models.EmailField(max_length=70, blank=True, default="example@gmail.com")
    product_image = models.ImageField(null=False, blank=False, upload_to='images/', default="default.jpg")
    name = models.CharField(max_length=64, default="name")

    def __str__(self):
        return self.title + ' | ' + str(self.name)