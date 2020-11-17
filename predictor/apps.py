from django.apps import AppConfig
from django.conf import settings
import os
import pickle


class PredictorConfig(AppConfig):
    # create path to models
    path = os.path.join(settings.MODELS, 'mex_model.pkl')

    # load models into separate variables
    # these will be accessible via this class
    with open(path, 'rb') as pickled:
        mexican_predictor = pickle.load(pickled)

    new_path=os.path.join(settings.MODELS, 'full_pipeline.pkl')

    with open(new_path, 'rb') as pickled2:
        data_pipeline= pickle.load(pickled2)

