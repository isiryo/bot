from django.db import models

# Create your models here.

class talk_past(models.Model):
    massage = models.CharField(max_length=256)
    massege_back= models.CharField(max_length=256)
    date=models.DateTimeField()
    massenger_name=models.CharField(max_length=64)
    class Meta:
        app_label="bot_app"



