from django.contrib import admin
<<<<<<<< HEAD:backend/notification/admin.py
from notification.models import Notification
========

from .models import Notification
>>>>>>>> main:backend/messagesTemp/admin.py

# Register your models here.
admin.site.register(Notification)
