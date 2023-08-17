from django.db import models

# from user.models import User
from expense.models import Expense


class IncomeCategory(models.Model):
    income_category_id = models.AutoField(primary_key=True)
    income_source = models.TextField()

    def __str__(self):
        return f"Source: {self.income_source}"


class Budget(models.Model):
    budget_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey("user.User", on_delete=models.CASCADE)
    budget_name = models.TextField()
    income_category_id = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Budget {self.budget_name}"

    @property
    def current_amount(self):
        expense_list = Expense.objects.filter(budget_id=self.budget_id)
        is_empty_list = expense_list == []
        if is_empty_list:
            return self.amount
        else:
            spending_amount = 0
            for expense in expense_list:
                spending_amount += expense.amount
            return self.amount - spending_amount
