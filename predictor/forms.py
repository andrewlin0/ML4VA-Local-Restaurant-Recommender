from django.forms import *
from .models import *


class UserAttributesForm(ModelForm):
    class Meta:
        model = UserAttributes
        fields = '__all__'
