import logging

from django.db import models
from notification.models import Notification

WARNING_BALANCE = 50000

logger = logging.getLogger(__name__)


class ExpenseCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    budget = models.ForeignKey("budget.Budget", on_delete=models.CASCADE)
    expense_category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_created=True)
    amount = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.expense_category.name + "--->" + self.budget.name

    def is_send_alert_email(self):
        notification_list = Notification.objects.filter(budget=self.budget)
        if (
            self.budget.current_amount <= WARNING_BALANCE
            and not self.budget.always_notify
        ):
            if notification_list == []:
                self.budget.send_alert_emails()
                return True
        elif (
            self.budget.current_amount <= WARNING_BALANCE and self.budget.always_notify
        ):
            self.budget.send_alert_emails()
            return True
        return False

    def save(self, *args, **kwargs):
        is_new = self._state.adding
        super().save(*args, **kwargs)
        if is_new:
            sending_status = self.is_send_alert_email()
