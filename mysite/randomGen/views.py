from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic
import json
from .models import Trick
from .forms import randomGenForm
import random

def home(request):
  form_class = randomGenForm
  context = {'form': form_class}

  return render(request, 'randomGen/index.html', context)

def generate(request):

  if request.method == 'POST':
    excl_Sonic = str_to_bool(request.POST.get('excl_Sonic'))
    excl_Palm = str_to_bool(request.POST.get('excl_Palm'))
    excl_family_choices = request.POST.get('excl_family_choices')
    desired_length = request.POST.get('the_length')
    response_data = {}
    all_trick_list = Trick.objects.all()
    if excl_Palm:
      all_trick_list = all_trick_list.exclude(name='Palm Spin')
    if excl_Sonic:
      all_trick_list = all_trick_list.exclude(family_choices = 'sonic')
    if excl_family_choices:
      all_trick_list = all_trick_list.exclude(family_choices = excl_family_choices)
    combo = [random.choice([trick.name + ' ' + trick.direction_choices for trick in all_trick_list]) for x in range(int(desired_length))]
    response_data['result'] = ' -> '.join(combo)
    response_data['name'] = 'Jack'
    response_data['all_trick_list'] = [trick.name for trick in all_trick_list]
    return JsonResponse(response_data)
  else:
    return JsonResponse({"ERROR": "error"})


def str_to_bool(s):
    if s == 'True' or s == 'true':
         return True
    elif s == 'False' or s == 'false':
         return False
    else:
         raise ValueError
  
