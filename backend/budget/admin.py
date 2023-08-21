from django.contrib import admin

from .models import Budget, IncomeCategory

# Register your models here.

# admin.site.register(Budget)


class BudgetAdmin(admin.ModelAdmin):
    list_display = (
        "user_id",
        "budget_name",
        "income_category_id",
        "amount",
    )

    # def get_current_amount(self, obj):
    #     return obj.current_amount

    # get_current_amount.short_description = "Current Amount"


admin.site.register(Budget, BudgetAdmin)
admin.site.register(IncomeCategory)
