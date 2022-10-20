from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms
from .models import Thing


class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea() }

        quantity = forms.CharField(
            widget=forms.NumberInput(),
            validators = [MinValueValidator(0), MaxValueValidator(50)]
        )
