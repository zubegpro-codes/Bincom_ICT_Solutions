from django.db import models

# Create your models here.
class DataEntry(models.Model):
    days = models.CharField(max_length=10, choices=[("Monday", "Monday"), ("Tuesday", "Tuesday"), ("Wednesday", "Wednesday"), ("Thursday", "Thursday"), ("Friday", "Friday"),],
        default=list,
        blank=True,
        null=True,)
    colorInputs = models.TextField(null=False, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

class ColorFreq(models.Model):
    name = models.CharField(max_length=200, null=True)
    freq = models.CharField(max_length=200, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

