from django.db import models
from django.utils import timezone


class Table(models.Model):
    table_number = models.CharField(max_length=50)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.table_number

class Reservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    number_of_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    message = models.TextField(blank=True)
    tables = models.ManyToManyField(Table)

    def __str__(self):
        return self.name


