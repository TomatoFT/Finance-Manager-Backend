from budget.models import Budget
from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.TextField()
    password = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)

    def __str__(self) -> str:
        return self.username

    @property
    def balance(self):
        budget_list = Budget.objects.filter(user_id=self.id)
        sum = 0
        for budget in budget_list:
            sum += budget.amount
        return sum
