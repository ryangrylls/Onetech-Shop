from django.contrib import admin
# Register your models here.
from .models import Category, Brand, Product, Payment, CartItem, Cart

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Payment)
admin.site.register(CartItem)
admin.site.register(Cart)