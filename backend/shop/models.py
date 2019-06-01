from django.db import models
from django.conf import settings
# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)

class Brand(models.Model):
    name = models.CharField(max_length=50)
    # category = models.ManyToManyField(Category)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    model = models.CharField(max_length=20, blank=True)
    description = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='products/', blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default="category")
    def __str__(self):
        return self.name

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(max_length=50)

class CartItem(models.Model):
    total_cost = models.DecimalField(max_digits=12, decimal_places=2)
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class Cart(models.Model):
    total_cost = models.DecimalField(max_digits=19, decimal_places=2)
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# class Customer(models.Model):
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     address = models.CharField(max_length=100, blank=True)
#     last_name = models.CharField(max_length=50)
#     first_name = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)

