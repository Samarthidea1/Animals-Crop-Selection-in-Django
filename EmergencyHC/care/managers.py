
import json




class CustomerQuerySet(models.QuerySet):
    def animals(self):
        return self.filter(role='A')

    def crops(self):
        return self.filter(role='C')

class CustomerManager(models.Manager):
    def get_queryset(self):
        return CustomereQuerySet(self.model, using=self._db)

    def animals(self):
        return self.get_queryset().animals()

    def crops(self):
        return self.get_queryset().crops()

class Customer(models.Model):
    ...
    choices_for_customers = (
        ("A", "Animals"),
        ("C", "Crops"),
    )
    ....
    choice_made = models.CharField(max_length=1, choices=choices_for_customers)

    all_customers = CustomerManager()