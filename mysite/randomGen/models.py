from __future__ import unicode_literals
import datetime
from django.db import models
from model_utils import Choices
from django.utils import timezone
from .choices import *

# Create your models here.
class Trick(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    # T1, T2, 12, 13, 14, 23, 24, 34, P 
    # DIRECTION_CHOICES = Choices('Normal', 'Reverse')
    direction_choices = models.CharField(choices=DIRECTION_CHOICES, default=DIRECTION_CHOICES.Normal, max_length=10)
    # ORIENT_CHOICES = Choices('Down', 'Up', 'Side', 'All')
    orient_choices = models.CharField(choices=ORIENT_CHOICES, default=ORIENT_CHOICES.All, max_length = 10)
    # POSITION_CHOICES = Choices('fingers','thumb', 'palm')
    position_choices = models.CharField(choices=POSITION_CHOICES, default=POSITION_CHOICES.thumb, max_length=10)
    # FAMILY_CHOICES = Choices('top', 'aerials', 'around', 'sonic', 'shadow', 'tap', 'pass', 'other')
    family_choices = models.CharField(choices=FAMILY_CHOICES, default=FAMILY_CHOICES.top, max_length=20)

    def __str__(self):
        return self.name + ' ' + self.direction_choices 

    # ADD Abbreviation attribute, add revolutions
    #filtering