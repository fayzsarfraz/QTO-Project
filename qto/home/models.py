from django.db import models

# Create your models here.
class Project(models.Model):
    name=models.CharField(max_length=200)
    des=models.TextField()
    date=models.DateField()
    status=models.CharField(max_length=20)
    
    def __str__(self):
        return self.name 
  