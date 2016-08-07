from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone
from django.views.decorators.csrf import ensure_csrf_cookie
from django.template import RequestContext
import json

from .models import Trick
from .forms import randomGenForm
import random


# class IndexView(generic.FormView):
#     template_name = 'randomGen/index.html'
#     #context_object_name = 'latest_tricks_list'
#     form_class = randomGenForm
#     success_url = ''

#     def form_valid(self, form):
#       return 1

    # def get_queryset(self):
    #   """
    #   Return 
    #   """

    #   return [1,2,3]#Trick.objects.all()

def home(request):
  form_class = randomGenForm
  context = {'form': form_class}

  return render(request, 'randomGen/index.html', context)

#@ensure_csrf_cookie

def generate(request):
  
  #context = {'all_trick_list': all_trick_list, 'form': form_class}
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
    #combo = desired_length
    combo = [random.choice([trick.name + ' ' + trick.direction_choices for trick in all_trick_list]) for x in range(int(desired_length))]
    response_data['result'] = ' -> '.join(combo)
    response_data['name'] = 'Jack'
    response_data['all_trick_list'] = [trick.name for trick in all_trick_list]
    return JsonResponse(response_data)
  else:
    return JsonResponse({"ERROR": "error"})
    # return HttpResponse(
    #   json.dumps(response_data),
    #   content_type="application/json"
    #   )
  # # else:
  #   return HttpResponse(
  #     json.dumps({"nothing to see": "this isn't happening"}),
  #     content_type="application/json"
  #     )

  # context = {'all_trick_list': all_trick_list, 'form': form_class}
  # return render(request, 'randomGen/index.html', context, RequestContext(request))

  # return render(request, 'randomGen/index.html', context)

def str_to_bool(s):
    if s == 'True' or s == 'true':
         return True
    elif s == 'False' or s == 'false':
         return False
    else:
         raise ValueError
  


  # def get_length(request):
  #     if request.method == 'POST':
  #       form = randomGenForm(request.POST)
  #       if form.is_valid():
  #         return HttpResponseRedirect(' / ')

  #     else:
  #       form = randomGenForm()

  #     return render(request, 'index.html', {'form': form})