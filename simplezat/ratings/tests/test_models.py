from django.test import TestCase

from ..models import Rating


class RatingTest(TestCase):
    def test_save_rating(self):
        rating = Rating()
        rating.sentiment = 'positive'
        rating.comment = 'You did great!'
        rating.save()

        rating = Rating.objects.last()
        self.assertEqual(rating.sentiment, 'positive')
        self.assertEqual(rating.comment, 'You did great!')
