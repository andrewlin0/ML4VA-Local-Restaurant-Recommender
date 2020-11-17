from sklearn.preprocessing import OneHotEncoder, StandardScaler, OrdinalEncoder
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from .apps import PredictorConfig
# import pandas


def our_pipeline(userinput):
    return PredictorConfig.data_pipeline.transform(userinput)

#
# #Encoders
# onehot = OneHotEncoder()
# ordinal = OrdinalEncoder()
#
# #Data
# tobe_ordinal = list(full[["drink_level", "dress_preference"]])
#
# user_cat = list(full[["ambience", "transport", "marital_status", "hijos",
#                            "interest", "personality", "religion", "color", "activity", "budget"]])
#
# user_num = list(full[["age", "wh_ratio"]])
#
#
# #Pipelines
# num_pipeline = Pipeline([
#         ('imputer', SimpleImputer(strategy="median")),
#         ('std_scaler', StandardScaler()),
#     ])
#
# full_pipeline = ColumnTransformer([
#         ("num", num_pipeline, user_num),
#         ("ordcat", ordinal, tobe_ordinal),
#         ("hotcat", onehot, user_cat),
#     ])
#
# #Prepared Data
# user_prepared = full_pipeline.transform(passin)
#
