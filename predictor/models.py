from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

SMOKECHOICES=[
    ('True', 'True'),
    ('False', 'False')
]

DRINK_CHOICES=[
    ('Abstemious', 'Abstemious'),
    ('Social Drinker', 'Social Drinker'),
    ('Casual Drinker', 'Casual Drinker'),
]

DRESS_CHOICES=[
    ('Formal', 'Formal'),
    ('Informal', 'Informal'),
    ('No Preference', 'No Preference')
]

AMBIENCE_CHOICES=[
    ('Family', 'Family'),
    ('Friends', 'Friends'),
    ('Solitary', 'Solitary')
]

TRANSPORT_CHOICES=[
    ('Car Owner', 'Car Owner'),
    ('Public', 'Public Transport'),
    ('On foot', 'On foot')
]

MARITAL_CHOICES=[
    ('Single', 'Single'),
    ('Married', 'Married'),
    ('Widow', 'Widow')
]

CHILDREN_CHOICES=[
    ('Independent', 'Independent'),
    ('Dependent', 'Dependent'),
    ('Kids', 'Kids')
]

INTEREST_CHOICES=[
    ('Technology', 'Technology'),
    ('Eco-Friendly', 'Eco-Friendly'),
    ('Retro', 'Retro'),
    ('Variety', 'Variety'),
    ('None', 'None')
]

PERSONALITY_CHOICES=[
    ('hard-worker', 'Hard-worker'),
    ('hunter-ostentatious', 'Hunter-ostentatious'),
    ('thrifty-protector', 'Thrifty-protector'),
    ('conformist', 'Conformist'),
]

RELIGION_CHOICES=[
    ('Christian', 'Christian'),
    ('Jewish', 'Jewish'),
    ('Muslim', 'Muslim'),
    ('Mormon', 'Mormon'),
    ('Other', 'Other'),
    ('None', 'None')
]

ACTIVITY_CHOICES=[
    ('Student', 'Student'),
    ('Professional', 'Professional'),
    ('Unemployed', 'Unemployed')
]

COLOR_CHOICES=[
    ('red', 'Red'),
    ('black', 'Black'),
    ('green', 'Green'),
    ('orange', 'Orange'),
    ('purple', 'Purple'),
    ('white', 'White'),
    ('blue', 'Blue'),
    ('yellow', 'Yellow')
]

BUDGET_CHOICES=[
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High')
]

class UserAttributes(models.Model):
    smoker=models.CharField(max_length=200, choices=SMOKECHOICES, default="")
    drink_level=models.CharField(max_length=200, choices=DRINK_CHOICES, default="")
    dress_preference=models.CharField(max_length=200, choices=DRESS_CHOICES, default="")
    ambience=models.CharField(max_length=200, choices=AMBIENCE_CHOICES, default="")
    transport=models.CharField(max_length=200, choices=TRANSPORT_CHOICES, default="")
    marital_status=models.CharField(max_length=200, choices=MARITAL_CHOICES, default="")
    children=models.CharField(max_length=200, choices=CHILDREN_CHOICES, default="")
    interest=models.CharField(max_length=200, choices=INTEREST_CHOICES, default="")
    personality=models.CharField(max_length=200, choices=PERSONALITY_CHOICES, default="")
    religion=models.CharField(max_length=200, choices=RELIGION_CHOICES, default="")
    activity=models.CharField(max_length=200, choices=ACTIVITY_CHOICES, default="")
    fav_color=models.CharField(max_length=200, choices=COLOR_CHOICES, default="")
    weight=models.IntegerField(validators=[MinValueValidator(25), MaxValueValidator(500)])
    budget=models.CharField(max_length=200, choices=BUDGET_CHOICES, default="")
    height=models.FloatField(validators=[MinValueValidator(0.5), MaxValueValidator(2.2)])
    age = models.IntegerField(default=20, validators=[MinValueValidator(1), MaxValueValidator(100)])
