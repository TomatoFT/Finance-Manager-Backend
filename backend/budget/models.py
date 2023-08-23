from django.db import models

# from user.models import User
# from expense.models import Expense
# from notification.models import Notification
from notification.serializers import NoticationSerializer

WARNING_BALANCE = 50000


class IncomeCategory(models.Model):
    id = models.AutoField(primary_key=True)
    source = models.TextField()

    def __str__(self):
        return f"Source: {self.source}"


class Budget(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    name = models.TextField()
    income_category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField(default=0)
    always_notify = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Budget {self.name}"

    def send_alert_emails(self):
        email = {
            "budget_id": self.id,
            "content": f"Your {self.name} has the amount less than 50000. \
                        The current amount is {self.amount}",
        }
        email_send = NoticationSerializer(data=email)
        if email_send.is_valid():
            email_send.save()
