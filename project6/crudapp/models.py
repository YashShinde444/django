# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    emobile = models.CharField(max_length=20)
    def __str__(self):
        return self.ename
