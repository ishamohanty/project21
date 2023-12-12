from django.db import models

# Create your models here.
class Country2(models.Model):
    countryID=models.IntegerField(primary_key=True)
    cname=models.CharField(max_length=100)
    population=models.IntegerField(max_length=20)
    def __str__(self):
        return self.countryID

class Capital2(models.Model):
    capitalID=models.IntegerField()
    c_name=models.CharField(max_length=10,primary_key=True)
    countryID=models.ForeignKey(Country2,on_delete=models.CASCADE)
    def __str__(self):
        return self.c_name


    


    
