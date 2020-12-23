from django.db import models
from django.contrib.auth.models import User


class StaffProfile(models.Model):
    StaffID = models.CharField(max_length=9, unique=True)    # StaffID เก็บรหัสพนักงาน
    Nickname = models.CharField(max_length=20)  # Nickname เก็บชื่อเล่น
    Position = models.CharField(max_length=20)  
    DepartmentName = models.CharField(max_length=40)
    DepartmentCode = models.CharField(max_length=30)
    WorkAge = models.IntegerField(default=0)
    Status = models.CharField(max_length=50)
    CreateDate = models.DateTimeField(auto_now=True)
    
   

class CollectStar(models.Model):
    StarID = models.AutoField(primary_key=True)
    Comment = models.CharField(max_length=300)
    StarAmount = models.IntegerField(default=0)
    YellowCard = models.IntegerField(default=0)
    Status = models.CharField(max_length=50)
    CreateDate = models.DateTimeField(auto_now=True)

class CollectStaff(models.Model):
    StaffID = models.ForeignKey(StaffProfile, related_name='StaffIDs', on_delete=models.CASCADE)
    StarID = models.ForeignKey(CollectStar, related_name='StarIDs', on_delete=models.CASCADE)
    CreateDate = models.DateTimeField(auto_now=True)


# comment status 0 = off 1 = on