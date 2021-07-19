from django.db import models

# Create your models here.
gender = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)


class Ems(models.Model):
    name = models.CharField(max_length=20)
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=40)
    address = models.CharField(max_length=10)
    gender = models.CharField(max_length=10, choices=gender)
    date = models.DateField()

    def __str__(self):
        return self.name
