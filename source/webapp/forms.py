from django import forms
from .models import Poll, Choice, Answer


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['text']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['choice']
        widgets = {'choice': forms.RadioSelect}
