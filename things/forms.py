"""Forms of the project."""
from django import forms
#from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Thing

# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        # The class variable 'model' is recognised by django as a class (not object)
        # by assigning model the class 'Thing', when django invokes the constructor of model
        # e.g. model() it is actually invoking the constructor of Thing e.g. Thing()
        # We have effectively localy changed the name of the class 'Thing' to be 'model'
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea()}
