# models.py
from django.db import models
 
class Test(models.Model):
    name = models.CharField(max_length=20)

class usr_t(models.Model):#用户
    objects = models.Manager()
    usr_name = models.CharField(max_length=30, primary_key=True, unique=True)
    usr_password = models.CharField(max_length=30)
    power = models.IntegerField()
    laboratory = models.CharField(max_length = 30)

class device(models.Model):#设备
    objects = models.Manager()
    id = models.IntegerField(primary_key = True, unique = True)
    device_name = models.CharField(max_length = 30)
    device_time = models.DateTimeField()
    buy_name = models.CharField(max_length = 30)
    laboratory = models.CharField(max_length = 30)

class appoint(models.Model):#预约
    objects = models.Manager()
    id = models.IntegerField(primary_key = True, unique = True)
    usr_name = models.CharField(max_length = 30)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    hour = models.IntegerField()
    device_id = models.IntegerField()
    

    
    