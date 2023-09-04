from django.contrib import admin

from .models import Budget, IncomeCategory

# Register your models here.

# admin.site.register(Budget)


class BudgetAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "income_category", "amount", "get_current_amount")

    def get_current_amount(self, obj):
        return obj.current_amount

    get_current_amount.short_description = "Current Amount"


admin.site.register(Budget, BudgetAdmin)
admin.site.register(IncomeCategory)
