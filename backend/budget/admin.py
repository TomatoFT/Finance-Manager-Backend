from django.contrib import admin

from .models import Budget, IncomeCategory

# Register your models here.

admin.site.register(Budget)
admin.site.register(IncomeCategory)
