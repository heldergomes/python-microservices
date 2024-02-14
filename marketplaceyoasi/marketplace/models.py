from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    email = models.CharField()
    password = models.CharField()


class Seller(models.Model):
    name = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18)
    phone = models.CharField(max_length=16)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
