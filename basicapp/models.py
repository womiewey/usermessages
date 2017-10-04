from django.db import models

# Create your models here.

class Messages(models.Model):
    name = models.CharField(max_length=50)
    mymessage = models.CharField(max_length=500)

    def __str__(self):
        return self.name,mymessage
    class Meta:
        verbose_name_plural = 'Messages' 