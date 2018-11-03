from django.db import models
# !/usr/bin/python
# coding:utf-8

from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

# Create your models here.
