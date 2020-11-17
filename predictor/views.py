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
from .kaleb import get_restaurant
from .pipeline import our_pipeline


def index(request):
    return render(request, "predictor/index.html")


def classify_me(request, target=None):
    if request.method == 'POST':  # Form has just been filled out
        form = UserAttributesForm(request.POST)
        if form.is_valid():

            user_input = form.save()

            location = user_input.location
            smoker = user_input.smoker
            drink_level = user_input.drink_level
            dress_preference = user_input.dress_preference
            ambience = user_input.ambience
            transport = user_input.transport
            marital_status = user_input.marital_status
            hijos = user_input.children
            interest = user_input.interest
            personality = user_input.personality
            religion = user_input.religion
            activity = user_input.activity
            color = user_input.fav_color
            weight = user_input.weight
            budget = user_input.budget
            height = user_input.height
            age = user_input.age
            ratio = weight / height

            preliminary_list = [bool(smoker), drink_level, dress_preference, ambience, transport, marital_status, hijos,
                                interest, personality,
                                religion, activity, color, budget, age, ratio]

            preliminary_list = np.asarray(preliminary_list)

            pred_frame = pd.DataFrame([preliminary_list],
                                      columns=["smoker", "drink_level", "dress_preference", "ambience", "transport",
                                               "marital_status",
                                               "hijos", "interest", "personality", "religion", "activity", "color",
                                               "budget", "age", "wh_ratio"])

            cleaned_data = our_pipeline(pred_frame)

            # Clean data and predict
            cuisine_recommendations = []

            mexican_model = PredictorConfig.mexican_predictor
            mexican_prediction = mexican_model.predict(cleaned_data)

            if mexican_prediction[0] == 1:
                cuisine_recommendations.append("Mexican")

            american_model = PredictorConfig.american_model
            american_prediction = american_model.predict(cleaned_data)

            if american_prediction[0] == 1:
                cuisine_recommendations.append("American")

            italian_model = PredictorConfig.italian_model
            italian_prediction = italian_model.predict(cleaned_data)

            if italian_prediction[0] == 1:
                cuisine_recommendations.append("Italian")

            des_model = PredictorConfig.dessert_model
            dessert_prediction = des_model.predict(cleaned_data)

            if dessert_prediction[0] == 1:
                cuisine_recommendations.append("Dessert/Cafe")

            asian_model = PredictorConfig.asian_model
            asian_prediction = asian_model.predict(cleaned_data)

            if asian_prediction[0] == 1:
                cuisine_recommendations.append("Asian")

            modern_model = PredictorConfig.modern_model
            modern_prediction = modern_model.predict(cleaned_data)
            if modern_prediction[0] == 1:
                cuisine_recommendations.append("Modern")

            me_model = PredictorConfig.me_model
            me_prediction = me_model.predict(cleaned_data)
            if me_prediction[0] == 1:
                cuisine_recommendations.append("Mediterranean/Middle East")

            euro_model = PredictorConfig.euro_model
            euro_prediction = euro_model.predict(cleaned_data)
            if euro_prediction[0] == 1:
                cuisine_recommendations.append("European")

            all_recommendations = []
            for cuisine in cuisine_recommendations:
                restaurant_recommendations = get_restaurant(location, cuisine, Main_dict, True)
                all_recommendations.append(restaurant_recommendations)

            return render(request, 'predictor/prediction.html',
                          context={'cuisines': cuisine_recommendations, 'restaurants': all_recommendations})
        else:
            form = UserAttributesForm(request.POST)
            return render(request, 'predictor/classifyme.html', context={'form': form})
    else:
        form = UserAttributesForm()
        return render(request, 'predictor/classifyme.html', context={'form': form})
