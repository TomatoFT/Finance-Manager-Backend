from django.contrib import admin
<<<<<<<< HEAD:backend/messagesTemp/admin.py

from .models import Notification
========
from notification.models import Notification
>>>>>>>> dev:notification/admin.py

# Register your models here.
admin.site.register(Notification)
