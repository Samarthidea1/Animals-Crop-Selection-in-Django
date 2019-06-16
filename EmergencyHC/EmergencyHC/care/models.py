from django.db import models

class Animal(models.Model):
    

    name_of_animal = models.CharField(max_length=30)
    city = models.CharField(max_length=10)
    mob_no = models.CharField(max_length=15)
    e_mail = models.CharField(max_length=20)

class Crop(models.Model):

    name = models.CharField(max_length=30)
    place = models.CharField(max_length=10)
    mob = models.CharField(max_length=15)
    mail = models.CharField(max_length=20)
        






