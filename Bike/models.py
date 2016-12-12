from django.db import models

# Create your models here.

class Person(models.Model):
    PersonName = models.CharField(max_length  = 20)
    PersonPassWord = models.CharField(max_length = 20)
    PersonGender = models.CharField(max_length = 2)
    PersonPhone = models.CharField(max_length = 20)
    PersonStatus = models.CharField(max_length = 2)
    AccountPayable = models.CharField(max_length = 20)#FloatField(max_digits = 11,decimal_places = 2)
    IsAdmin = models.FloatField()
    
    def __unicode__(self):
        return self.PersonName

class Bike(models.Model):
    BikeType = models.CharField(max_length = 20)
    BikeStatus = models.CharField(max_length = 2)
    BikeUnitPrice = models.CharField(max_length = 20)#FloatField(max_digits=11,decimal_places=2)
    
    def __unicode__(self):
        return self.BikeType
    
class Order(models.Model):
    OrderPersonID = models.ForeignKey(Person)
    OrderBikeID = models.ForeignKey(Bike)
    OrderStartTime = models.CharField(max_length = 30)#DateField(auto_now_add='true')
    OrderEndTime = models.CharField(max_length = 30)#DateField()
    OrderAccountPayable = models.CharField(max_length = 20)#FloatField(max_digits=11,decimal_places=2)
    
    def __unicode__(self):
        return self.OrderStartTime