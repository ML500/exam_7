from django import forms
from .models import Poll, Choice


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['text']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']
