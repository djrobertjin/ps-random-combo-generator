from model_utils import Choices


blank_choice = Choices('')
DIRECTION_CHOICES = Choices('Normal', 'Reverse')
ORIENT_CHOICES = Choices('Down', 'Up', 'Side', 'All')
POSITION_CHOICES = Choices('fingers','thumb', 'palm')
FAMILY_CHOICES = Choices('top', 'aerials', 'around', 'sonic', 'tap', 'pass', 'other')