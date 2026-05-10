from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class BrandManager(models.Manager):
    def search(self,name):
        return self.filter(slug__icontains = name)


class Brand(models.Model):
    name = models.CharField(max_length=40,primary_key=True)
    tagline = models.TextField()
    slug = AutoSlugField(populate_from='name')
    objects = BrandManager()
    class Meta:
        db_table = "brand"
    def __str__(self):
        return f"name : {self.name}  |  tagline : {self.tagline}"


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/category/',default=r'\category\c1.jpg')

class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name',blank=True,unique=True,null=True)
    price = models.DecimalField(decimal_places=2,max_digits=12)
    description = models.TextField(default='')
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    category = models.ManyToManyField(to=Category)
    quantity =  models.IntegerField(default=1)
    image = models.ImageField(upload_to='images/products/',default=r'\products\p7.jpg')
    def __str__(self):
        return f'({self.name}) from {self.brand.name}'
    class Meta:
        db_table = 'Product'
        ordering = ["name","-price"]



class ProductImages(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/product/images')
    def __str__(self) -> str:
        return f'image of {self.product.name}'
    class Meta:
        db_table = 'Product_Images'
