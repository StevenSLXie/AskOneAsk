from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ans(models.Model):
    answer = models.TextField()
    person = models.TextField()


class Qns(models.Model):
    qns = models.TextField() 
    author = models.ForeignKey(User,null=True,blank=True)
    answerSet = models.ManyToManyField(Ans)


