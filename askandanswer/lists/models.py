from django.db import models
from django.contrib.auth.models import User
#from django.db.models.signals import post_save

# Create your models here.

class Person(models.Model):
    user = models.OneToOneField(User)
    city = models.TextField(default='Earth',editable=False)
    status = models.BooleanField(default=True,editable=False)

    def name(self):
        return self.user.username

    def email(self):
        return self.user.email

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





