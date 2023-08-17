from django.db import models

# from user.models import User
# from budget.models import Budget


# Create your models here.
class ExpenseCategory(models.Model):
    expense_category_id = models.AutoField(primary_key=True)
    expense_category_name = models.TextField()

    def __str__(self) -> str:
        return f"{self.expense_category_name}"


class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    budget_id = models.ForeignKey("budget.Budget", on_delete=models.CASCADE)
    expense_category_id = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_created=True)
    amount = models.PositiveIntegerField()

    def __str__(self) -> str:
        return super().__str__()
