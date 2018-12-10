from django import forms

from .models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = [
            'sentiment',
            'comment'
        ]
        widgets = {
            'sentiment': forms.HiddenInput()
        }
        error_messages = {
            'comment': {
                'required': 'Please wrirte some comment..'
            },
        }
