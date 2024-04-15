# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FlagModel(models.Model):
    forward_flag = models.BooleanField(default=False)
    forward_left_flag = models.BooleanField(default=False)
    forward_right_flag = models.BooleanField(default=False)
    left_flag = models.BooleanField(default=False)
    right_flag = models.BooleanField(default=False)
    brake_flag = models.BooleanField(default=False)
    reverse_flag = models.BooleanField(default=False)
    reverse_right_flag = models.BooleanField(default=False)
    reverse_left_flag = models.BooleanField(default=False)
