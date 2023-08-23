from budget.models import Budget
from django.db import models
from notification.models import Notification

WARNING_BALANCE = 50000


class ExpenseCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    budget = models.ForeignKey(Budget, on_delete=models.CASCADE)
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_created=True)
    amount = models.PositiveIntegerField()

    def __str__(self) -> str:
        return super().__str__()

    def update_amount_in_budget(self):
        budget = Budget.objects.get(id=self.budget.id)
        notification_list = Notification.objects.filter(id=self.id)
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
