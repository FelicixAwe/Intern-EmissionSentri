from django.contrib import admin
from .models import Emission


@admin.register(Emission)
class EmissionAdmin(admin.ModelAdmin):
    list_display = ['date_created', 'accounting_period',
                    'scope1', 'scope2', 'scope3']
