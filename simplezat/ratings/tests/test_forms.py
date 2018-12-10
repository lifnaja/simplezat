from django import forms
from django.test import TestCase

from ..forms import RatingForm
from ..models import Rating

class RatingFormTest(TestCase):
    def setUp(self):
        self.form = RatingForm()

    def test_form_should_have_defined_fields(self):
        expected_fields = [
            'sentiment',
            'comment',
        ]
        for each in expected_fields:
            self.assertTrue(each in self.form.fields)

    def test_form_should_have_correct_fields_and_widget(self):
        self.assertIsInstance(
            self.form.fields['sentiment'].widget,
            forms.HiddenInput
        )
        self.assertIsInstance(
            self.form.fields['comment'].widget,
            forms.Textarea
        )

    def test_form_with_invalid_input_should_be_invalid(self):
        data = {
            'sentiment': 'positive',
            'comment': ''
        }
        form = RatingForm(data=data)
        self.assertFalse(form.is_valid())

        expected = {
            'comment': ['Please wrirte some comment..']
        }
        self.assertEqual(form.errors, expected)

    def test_form_with_valid_input_should_be_valid(self):
        data = {
            'sentiment': 'positive',
            'comment': 'You did great!'
        }
        form = RatingForm(data=data)
        self.assertTrue(form.is_valid())

    def test_form_with_valid_input_saved_should_be_save_data(self):
        data = {
            'sentiment': 'positive',
            'comment': 'You did great!'
        }
        form = RatingForm(data=data)
        form.is_valid()
        form.save()

        rating = Rating.objects.last()
        self.assertEqual(rating.sentiment, 'positive')
        self.assertEqual(rating.comment, 'You did great!')
