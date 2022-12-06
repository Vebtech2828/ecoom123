from django.db import models


class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=64)
    esal = models.FloatField()
    eaddr = models.CharField(max_length=64)

class JobData(models.Model):
    jposting = models.DateTimeField()
    jlocation = models.TextField()
    joffersal = models.IntegerField()
    jquali = models.TextField()

    # def __str__(self):
    #     return self.jposting

# Table Name= paytm1_Employee
# Field Name = eno,ename,esal,eaddr
# Behavior = int , char , Float, Char (Max allowed - 64)