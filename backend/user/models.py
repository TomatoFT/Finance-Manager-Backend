from budget.models import Budget
from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.TextField()
    password = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    # user_balance = models.PositiveIntegerField()

    def __str__(self) -> str:
        return self.username

    @property
    def balance(self):
        budget_list = Budget.objects.filter(user_id=self.user_id)
        sum = 0
        for budget in budget_list:
            sum += budget.amount
        return sum
