from django.forms import *
from .models import *


class UserAttributesForm(ModelForm):
    class Meta:
        model = UserAttributes
        fields = '__all__'

        widgets = {
            'height': TextInput(attrs={'placeholder': 'Enter your weight in Kilograms'}),
            'weight': TextInput(attrs={'placeholder': 'Enter your height in Meters'}),
        }

