from django import forms
from .models import Trick
from .choices import *

class randomGenForm(forms.Form):
    length = forms.IntegerField(label= 'length', initial = 5, min_value = 2, max_value = 10, required=True)
    excl_Palm = forms.BooleanField(initial = False)
    excl_Sonic = forms.BooleanField(initial = False)
    excl_family_choices = forms.MultipleChoiceField(choices = blank_choice + FAMILY_CHOICES, required = False, widget = forms.Select())
    #name = forms.CharField(required=True)