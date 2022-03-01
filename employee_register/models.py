from django.db import models

# Create your models here.
class Position(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    emp_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
