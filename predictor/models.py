from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

SMOKECHOICES=[
    ('True', 'True'),
    ('False', 'False')
]

DRINK_CHOICES=[
    ('abstemious', 'Abstemious'),
    ('social drinker', 'Social Drinker'),
    ('casual drinker', 'Casual Drinker'),
]

DRESS_CHOICES=[
    ('formal', 'Formal'),
    ('informal', 'Informal'),
    ('no preference', 'No Preference')
]

AMBIENCE_CHOICES=[
    ('family', 'Family'),
    ('friends', 'Friends'),
    ('solitary', 'Solitary')
]

TRANSPORT_CHOICES=[
    ('car owner', 'Car Owner'),
    ('public', 'Public Transport'),
    ('on foot', 'On foot')
]

MARITAL_CHOICES=[
    ('single', 'Single'),
    ('married', 'Married'),
    ('widow', 'Widow')
]

CHILDREN_CHOICES=[
    ('independent', 'Independent'),
    ('dependent', 'Dependent'),
    ('kids', 'Kids')
]

INTEREST_CHOICES=[
    ('technology', 'Technology'),
    ('eco-friendly', 'Eco-Friendly'),
    ('retro', 'Retro'),
    ('variety', 'Variety'),
    ('none', 'None')
]

PERSONALITY_CHOICES=[
    ('hard-worker', 'Hard Worker'),
    ('hunter-ostentatious', 'Extrovert'),
    ('thrifty-protector', 'Introvert'),
    ('conformist', 'Conformist'),
]

RELIGION_CHOICES=[
    ('Christian', 'Christian'),
    ('Jewish', 'Jewish'),
    ('Muslim', 'Muslim'),
    ('Other', 'Other'),
    ('none', 'None')
]

ACTIVITY_CHOICES=[
    ('student', 'Student'),
    ('professional', 'Professional'),
    ('unemployed', 'Unemployed')
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

LOCATION_CHOICES=[
    ('Charlottesville', 'Charlottesville'),
    ('NoVA', 'NoVA'),
    ('Roanoke', 'Roanoke'),
    ('Richmond', 'Richmond'),
    ('Virginia Beach', 'Virginia Beach'),
    ('Blacksburg', 'Blacksburg')
]

class UserAttributes(models.Model):
    location=models.CharField(max_length=200, choices=LOCATION_CHOICES, default="")
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
    height=models.FloatField(validators=[MinValueValidator(0.6), MaxValueValidator(2.2)])
    age = models.IntegerField(default=20, validators=[MinValueValidator(1), MaxValueValidator(100)])
    #hunger=models.IntegerField(default="")
