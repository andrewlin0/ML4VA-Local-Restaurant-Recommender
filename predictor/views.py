import numpy as np
from django.http import HttpResponse
from django.shortcuts import render
from .apps import PredictorConfig
from .forms import *
import pandas as pd
from django.http import JsonResponse
from rest_framework.views import APIView
# Create your views here.
from .kaleb import Main_dict

def index(request):
    return render(request, "predictor/index.html")

def classify_me(request, target=None):
    if request.method== 'POST': #Form has just been filled out
        form = UserAttributesForm(request.POST)
        if form.is_valid():
            user_input=form.save()
            location=user_input.location

            smoker = user_input.smoker
            drink_level = user_input.drink_level
            dress_preference = user_input.dress_preference
            ambience = user_input.ambience
            transport = user_input.transport
            marital_status = user_input.marital_status
            children = user_input.children
            interest = user_input.interest
            personality = user_input.personality
            religion = user_input.religion
            activity = user_input.activity
            fav_color = user_input.fav_color
            weight = user_input.weight
            budget = user_input.budget
            height = user_input.height
            age = user_input.age

            #print(Main_dict)
            #Clean data and predict
            mexican_model = PredictorConfig.mexican_predictor
            r = [0] * 41
            r.append(70)
            r.append(0)
            r.append(1.7)
            r.append(1)

            p = np.array(r)
            t = p.reshape(1, -1)
            mexican_prediction=mexican_model.predict(t)

            return HttpResponse("Prediction for Mexican Cuisine: "+str(mexican_prediction))
        else:
            form = UserAttributesForm(request.POST)
            return render(request, 'predictor/classifyme.html', context={'form': form})
    else:
        form= UserAttributesForm()
        return render(request, 'predictor/classifyme.html', context={'form': form})