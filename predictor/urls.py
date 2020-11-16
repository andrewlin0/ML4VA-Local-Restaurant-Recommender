from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views

appname = "predictor"
urlpatterns = [
    path('', views.index, name='index'),
    path('classifyme/', views.classify_me, name="classification")
]
