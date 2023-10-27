from django.db import models


class Emission(models.Model):
    date_created = models.DateField(auto_now_add=True)
    accounting_period = models.CharField(max_length=100)
    scope2 = models.IntegerField(null=True, blank=True)
    scope3 = models.IntegerField(null=True, blank=True)
    scope1 = models.IntegerField(null=True, blank=True)
