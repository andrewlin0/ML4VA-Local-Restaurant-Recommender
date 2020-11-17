from django.forms import *
from .models import *


class UserAttributesForm(ModelForm):
    class Meta:
        model = UserAttributes
        fields = '__all__'

        widgets = {
            'height': TextInput(attrs={'placeholder': 'Enter your height in meters'}),
            'weight': TextInput(attrs={'placeholder': 'Enter your weight in kilograms'}),
        }

    def clean_height(self):
        data = self.cleaned_data['height']
        if float(data)>2.2 or float(data)<1:
            raise ValidationError("Please enter a valid height in meters between 1 and 2.2 meters")
        return data

    def clean_weight(self):
        data = self.cleaned_data['weight']
        if float(data)<20 or float(data)>500:
            raise ValidationError("Please enter a valid whole number weight in Kilograms between 20 and 500kg")
        return data
