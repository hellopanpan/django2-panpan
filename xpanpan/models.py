from django.db import models
import mongoengine
# Create your models here.
# class Person(models.Model):
#     name = models.CharField(max_length=30)
#     age = models.IntegerField()

class Person(mongoengine.Document):
    name = mongoengine.StringField(max_length=30)
    age = mongoengine.IntField()