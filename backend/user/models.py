from django.db import models

# Create your models here.


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.TextField()
    user_password = models.TextField()
    user_email = models.EmailField()
    user_phone = models.CharField(max_length=12)
    # user_profile_picture = models.FilePathField(path ="media")
    user_balance = models.PositiveIntegerField()
