from django.db import models


class Notification(models.Model):

    notification_id = models.AutoField(primary_key=True)
    budget_id = models.ForeignKey("budget.Budget", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.budget_id}_{self.content}"
