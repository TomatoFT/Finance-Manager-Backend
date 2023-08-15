from django.db import models

class Notification(models.Model):
    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    # class Meta:
    #     app_label = 'messagesTemp'

    def __str__(self):
        return self.content