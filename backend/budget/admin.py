from budget.models import Budget, IncomeCategory
from django.contrib import admin


class BudgetAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "income_category", "amount", "get_current_amount")

    def get_current_amount(self, obj):
        return obj.current_amount

    get_current_amount.short_description = "Current Amount"


admin.site.register(Budget, BudgetAdmin)
admin.site.register(IncomeCategory)
