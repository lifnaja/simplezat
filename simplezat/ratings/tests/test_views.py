from django.test import TestCase
from django.urls import reverse

from ..models import Rating


class RatingViewTest(TestCase):
    def setUp(self):
        self.url = reverse('ratings')

    def test_rating_view_should_have_question_text(self):
        response = self.client.get(self.url)

        expected = '<h1>How do we do?</h1>'
        self.assertContains(response, expected, status_code=200)

    def test_rating_view_should_show_three_ratings(self):
        response = self.client.get(self.url)

        positive_url = reverse('comment', kwargs={'rating': 'positive'})
        expected = f'<a href="{positive_url}">' \
            '<img src="/static/images/positive.png" alt ="Positive"></a>'
        self.assertContains(response, expected, status_code=200)

        neutral_url = reverse('comment', kwargs={'rating': 'neutral'})
        expected = f'<a href="{neutral_url}">' \
            '<img src="/static/images/neutral.png" alt ="Nuetral"></a>'
        self.assertContains(response, expected, status_code=200)

        negative_url = reverse('comment', kwargs={'rating': 'negative'})
        expected = f'<a href="{negative_url}">' \
            '<img src="/static/images/negative.png" alt ="Negative"></a>'
        self.assertContains(response, expected, status_code=200)


class CommentViewTest(TestCase):
    def setUp(self):
        self.url = reverse(
            'comment',
            kwargs={
                'rating': 'positive'
            }
        )

    def test_comment_view_should_render_text_and_comment_form_correctly(self):
        for each in ['positive', 'abc']:
            url = reverse(
                'comment',
                kwargs={
                    'rating': each
                }
            )
            response = self.client.get(url)

            expected = '<h1>Any comment?</h1>'
            self.assertContains(response, expected, status_code=200)

            expected = '<form action="." method="post">' \
                '<input type="hidden" name="csrfmiddlewaretoken"'
            self.assertContains(response, expected, status_code=200)

            expected = '<p><label for="id_comment">Comment:</label>' \
                '<textarea name="comment" cols="40" rows="10" required ' \
                'id="id_comment"></textarea><input type="hidden" ' \
                f'name="sentiment" value="{ each }" id="id_sentiment"></p>' \
                '<input type="submit" value="Submit"></form>'

            self.assertContains(response, expected, status_code=200)

    def test_submit_comment_form_should_save_data_and_redirect(self):
        data = {
            'sentiment': 'positive',
            'comment': 'You did great!'
        }

        response = self.client.post(self.url, data=data)

        self.assertRedirects(response, reverse('thanks'))

        rating = Rating.objects.last()
        self.assertEqual(rating.sentiment, 'positive')
        self.assertEqual(rating.comment, 'You did great!')

    def test_submit_comment_invalid_form_should_not_save_data_and_not_redirect(
        self
    ):
        data = {
            'sentiment': 'positive',
            'comment': ''
        }

        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, 200)

        rating = Rating.objects.last()
        self.assertIsNone(rating)


class ThankViewTest(TestCase):
    def test_thank_view_should_have_thnak_you_text(self):
        url = reverse('thanks')
        response = self.client.get(url)

        expected = '<h1>Thank you!</h1>'
        self.assertContains(response, expected, status_code=200)
