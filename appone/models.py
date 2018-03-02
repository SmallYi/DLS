from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.



# 一个作者对应多本书，一本书只有一个作者 外键（一对多）
class configure_lstm(models.Model):
    modelname = models.CharField(max_length=20, primary_key=True)
    baseline = models.CharField(max_length=20)
    baselineunit = models.CharField(max_length=20)
    train = models.CharField(max_length=100)
    baselinevalue = models.CharField(max_length=20)
    flag = models.IntegerField()
    class Meta:
        db_table = "configure_lstm"

class configure_relation(models.Model):
    modelname = models.CharField(max_length=20, primary_key=True)
    operationtype = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    minsupport =  models.CharField(max_length=20)
    minconfidence =  models.CharField(max_length=20)
    flag = models.IntegerField()
    class Meta:
        db_table = "configure_relation"
