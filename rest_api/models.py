from django.db import models

# Create your models here.

class UserDetail(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    age = models.IntegerField()
    
    def __str__(self):
        return self.user_name
    
class MobileTable(models.Model):
    mobile_image = models.URLField(default="null")
    mobile_name = models.CharField(max_length=50)
    mobile_price = models.IntegerField()
    
    def __str__(self):
        return self.mobile_name