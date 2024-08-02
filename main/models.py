from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=30)
    materials = models.ManyToManyField('Material', through='Product_Material')

    def __str__(self):
        return self.name


class Material(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.PositiveBigIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Product_Material(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    material_id = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.product_id)
