# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
 
    def __str__(self):
        return str(self.name)+str(self.email) 