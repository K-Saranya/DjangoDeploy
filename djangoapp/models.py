from django.db import models

# Create your models here.

# class ProductDetails(models.Model):
#     product_name = models.CharField(max_length=100)
#     product_price = models.CharField(max_length=30)
#     product_description = models.CharField(max_length=100)
#     product_category = models.CharField(max_length=100)
#     product_image = models.CharField(max_length=200)
    
#     def __str__(self):
#         return self.product_name
    
# class ProductImage(models.Model):
#     product = models.CharField(max_length=50)

class Product_Table(models.Model):
    product_image = models.URLField()
    product_name = models.CharField(max_length=100)
    product_price  = models.IntegerField()