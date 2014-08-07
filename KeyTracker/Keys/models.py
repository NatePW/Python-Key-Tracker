from django.db import models

class Key(models.Model):
    name = models.CharField(max_length=15)
    color = models.CharField(max_length=15)
    def __unicode__(self):
        return self.name

class People(models.Model):
    name = models.CharField(max_length=25)
    active = models.BooleanField(default=1)
    def __unicode__(self):
        return self.name
    
class Checkout(models.Model):
    timeOut = models.DateTimeField('timeout')
    timeIn = models.DateTimeField('timein')
    isOut = models.BooleanField(default=1)
    key = models.ForeignKey(Key)
    people = models.ForeignKey(People)
    def __unicode__(self):
        return self.key