"""Unit tests for the Thing model."""
from django import forms
from django.test import TestCase
from .models import Thing
from .forms import ThingForm

class ThingModelTestCase(TestCase):
    """Unit tests for the Thing model."""

    def setUp(self):
        self.form_input = {
        'name' : 'Apple',
        'escription' : 'I am an apple',
        'quantity' : 10,
        'created_at' : '20/10/2022 20:26'
        }

    def test_valid_thing_form(self):
        form = ThingForm(data=self.form_input)
        self.assertTrue(form.is_valid())
