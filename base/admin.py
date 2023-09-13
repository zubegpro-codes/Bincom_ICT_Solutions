from django.contrib import admin

# Register your models here.
from .models import DataEntry, ColorFreq
admin.site.register(DataEntry)
admin.site.register(ColorFreq)
