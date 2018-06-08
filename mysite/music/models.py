# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Students(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50, blank=False, null=False)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return '%s' % self.id


class Log(models.Model):
    refid = models.ForeignKey(Students, on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    in_time = models.TimeField(null=False, blank=False)
    out_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return '%s' % self.refid
