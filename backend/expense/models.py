from budget.models import Budget
from django.db import models
from notification.models import Notification

WARNING_BALANCE = 50000


class ExpenseCategory(models.Model):
    expense_category_id = models.AutoField(primary_key=True)
    expense_category_name = models.TextField()

    def __str__(self) -> str:
        return f"{self.expense_category_name}"


class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    budget_id = models.ForeignKey(Budget, on_delete=models.CASCADE)
    expense_category_id = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_created=True)
    amount = models.PositiveIntegerField()

    def __str__(self) -> str:
        return super().__str__()

    def update_amount_in_budget(self):
        budget = Budget.objects.get(budget_id=self.budget_id.budget_id)
        notification_list = Notification.objects.get(budget_id=self.budget_id.budget_id)
        budget.amount -= self.amount
        budget.save()
        if budget.amount <= WARNING_BALANCE and not budget.always_notify:
            if notification_list == []:
                budget.send_alert_emails()
        elif budget.amount <= WARNING_BALANCE and budget.always_notify:
            budget.send_alert_emails()

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)
        if is_new:
            self.update_amount_in_budget()
