import numpy as np
from django.http import HttpResponse
from django.shortcuts import render
from .apps import PredictorConfig
from .forms import *
from django.http import JsonResponse
from rest_framework.views import APIView
# Create your views here.

def index(request):
    mexican_model=PredictorConfig.mexican_predictor
    r = [0] * 45
    r.append(70)
    r.append(0)
    r.append(1.7)
    r.append(1)

    p=np.array(r)
    t=p.reshape(1, -1)
    print(mexican_model.predict(t))

    return HttpResponse("This is where the predictor will go")

def classify_me(request, target=None):
    if request.method== 'POST': #Form has just been filled out
        form = UserAttributesForm(request.POST)
        form.fields['smoker'].initial = None
        if form.is_valid():
            user_input=form.save()
            #Clean data and predict
            return HttpResponse("Thank you for filling out the form")
        else:
            form = UserAttributesForm()
            form.fields['smoker'].initial = None
            return render(request, 'predictor/classifyme.html', context={'form': form})
    else:
        form= UserAttributesForm()
        form.fields['smoker'].initial = None
        return render(request, 'predictor/classifyme.html', context={'form': form})