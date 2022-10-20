from django import forms
from .models import Thing


class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description']
        widgets = {'description': forms.Textarea() }

        quantity = forms.CharField(label='Quantity', widget=forms.NumberInput())
