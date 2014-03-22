from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Person(models.Model):
    username = models.TextField()
    email = models.TextField()
    city = models.TextField()
    status = models.BooleanField()
    def __init__(self,user=None):
        if user == None:
            super(Person,self).__init__()
        else:
            self.username = user.username
            self.email = user.email

class Qns(models.Model):
    qns = models.TextField() 
    author = models.ForeignKey(User,null=True,blank=True)

class Ans(models.Model):
    answer = models.TextField()
    person = models.TextField()
    qns = models.ForeignKey(Qns)

    def getQns(self):
        return self.qns.qns
    def askedByWhom(self):
        return self.qns.author





