from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Opportunity)
admin.site.register(models.Tag)
admin.site.register(models.Interest)
admin.site.register(models.Research_help)