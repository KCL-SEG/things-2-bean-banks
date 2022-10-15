"""Forms of the project."""
from django import forms
#from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Thing

# Create your forms here.
class ThingsForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea()}
    #name = forms.charField(label="Name", max_length=35, unique=True))
    #description = forms.charField(label="Description", max_length=120, blank=True)
    #quantity = forms.charField(label="NumberInput", validators=[MinValueValidator(0),MaxValueValidator(50))
