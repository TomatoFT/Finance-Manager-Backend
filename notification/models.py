from django.db import models


class Notification(models.Model):

    id = models.AutoField(primary_key=True)
    budget = models.ForeignKey("budget.Budget", on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id}_{self.content}"
