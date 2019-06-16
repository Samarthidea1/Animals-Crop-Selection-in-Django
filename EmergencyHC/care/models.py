from django.db import models
from care.managers import CustomerQuerySet


class Customer(models.Model):
      gender_choices = (
           ("M", "Male"),
           ("F", "Female")
      )
      choices_for_customers = (
           ("C", "Crops"),
           ("A", "Animals"),
      )
      first_name = models.CharField(max_length=200)
      last_name = models.CharField(max_length=200)
      email = models.CharField(max_length=250)
      gender = models.CharField(max_length=1, choices=gender_choices)
      choice_made = models.CharField(max_length=120, choices=choices_for_customers, default="A")
      

      # custom manager replaces objects manger
      all_customers = models.Manager()

      def __str__(self):
            return str(self.first_name) + str(self.last_name)


 class CustomerManager(models.Manager):
        def get_queryset(self):
            return super(CustomerManager, self).get_queryset().filter(active=True)


class CropsManager(models.Manager):
    def get_queryset(self):
        return super(CropsManager, self).get_queryset().filter(role='C')

class AnimalsManager(models.Manager):
    def get_queryset(self):
        return super(AnimalsManager, self).get_queryset().filter(role='A')

class Customer(models.Model):
    ...
    choices_for_customers = (
        ("A", "Animals"),
        ("C", "Crops"),
    )
    ....
    choice_made = models.CharField(max_length=1, choices=choices_for_customers)

    all_customer = models.Manager()
    crops = CropsManager()
    animals = AnimalsManager()                    





