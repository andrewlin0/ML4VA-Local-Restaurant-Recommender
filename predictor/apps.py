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

    path3 = os.path.join(settings.MODELS, 'ameri_model.pkl')

    with open(path3, 'rb') as pickled3:
        american_predictor = pickle.load(pickled3)

    path4 = os.path.join(settings.MODELS, 'asi_model.pkl')

    with open(path4, 'rb') as pickled4:
        asian_model = pickle.load(pickled4)

    path5 = os.path.join(settings.MODELS, 'dc_model.pkl')

    with open(path5, 'rb') as pickled5:
        dessert_model = pickle.load(pickled5)

    path6 = os.path.join(settings.MODELS, 'euro_model.pkl')

    with open(path6, 'rb') as pickled6:
        euro_model = pickle.load(pickled6)

    path7 = os.path.join(settings.MODELS, 'ital_model.pkl')

    with open(path7, 'rb') as pickled7:
        italian_model = pickle.load(pickled7)

    path8 = os.path.join(settings.MODELS, 'mme_model.pkl')

    with open(path8, 'rb') as pickled8:
        me_model = pickle.load(pickled8)

    path9 = os.path.join(settings.MODELS, 'mod_model.pkl')

    with open(path9, 'rb') as pickled9:
        modern_model = pickle.load(pickled9)