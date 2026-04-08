from django.db import models

# Create your models here.
class State(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
class Gender(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Acc_type(models.Model):
    name = models.CharField(max_length=30)    

    def __str__(self):
        return self.name

class RelationShip(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Accounts(models.Model):
    acc_num  = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    dob = models.DateField()
    phone = models.BigIntegerField(unique=True)
    email = models.EmailField()
    aadhar = models.PositiveBigIntegerField()
    address = models.TextField()
    state  = models.ForeignKey(State,on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender,on_delete=models.CASCADE)
    acc_type = models.ForeignKey(Acc_type,on_delete=models.CASCADE)
    nomine_name = models.CharField(max_length=40)
    relation = models.ForeignKey(RelationShip,on_delete=models.CASCADE)
    balance = models.FloatField(default=1000)
    pin = models.CharField(max_length=64,default="0000")
    images = models.ImageField(upload_to="profiles")


