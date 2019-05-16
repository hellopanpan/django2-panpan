from django.db import models
import mongoengine
# Create your models here.
# class Person(models.Model):
#     name = models.CharField(max_length=30)
#     age = models.IntegerField()

class Person(mongoengine.Document):
    name = mongoengine.StringField(max_length=30)
    age = mongoengine.IntField()

class Movies(mongoengine.Document):
    title = mongoengine.StringField(max_length=30)
    link = mongoengine.StringField(max_length=30)
    desc = mongoengine.StringField(max_length=30)
