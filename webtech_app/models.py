from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class user_info(models.Model):
    email = models.EmailField(max_length=20,null=False,primary_key=True,default='')
    password = models.CharField(max_length=20,null=True)

    def __str__(self):
        return f"{self.email}"

class plot_info(models.Model):
    user_name = models.CharField(max_length=20,null=True)
    period1 = models.PositiveIntegerField()
    period2 = models.PositiveIntegerField(null=True)
    period3 = models.PositiveIntegerField(null=True)
    select1 = models.CharField(max_length=20)
    select2 = models.CharField(max_length=20)
    select3 = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    analysis_type = models.CharField(max_length=10,null=True)

    def __str__(self):
        return f"{self.user_name} - {self.analysis_type}"
