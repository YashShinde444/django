# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Users(models.Model):
    eid=models.CharField(max_length=50)
    ename=models.CharField(max_length=50)
    email=models.EmailField()
    econtact=models.CharField(max_length=50)
