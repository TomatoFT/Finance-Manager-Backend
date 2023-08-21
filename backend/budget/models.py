from django.db import models

# from user.models import User
# from expense.models import Expense
# from notification.models import Notification
from notification.serializers import MessageSerializer

WARNING_BALANCE = 50000


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
    amount = models.PositiveIntegerField(default=0)
    always_notify = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Budget {self.budget_name}"

    def send_alert_emails(self):
        email = {
            "budget_id": self.budget_id,
            "content": f"Your {self.budget_name} has the amount less than 50000. \
                        The current amount is {self.amount}",
        }
        email_send = MessageSerializer(data=email)
        if email_send.is_valid():
            email_send.save()
