from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse


class RatingView(View):
    template = 'ratings.html'

    def get(self, request):
        return render(
            request,
            self.template
        )


class CommentView(View):
    template = 'comments.html'

    def get(self, request, rating):
        return render(
            request,
            self.template,
            {
                'rating': rating
            }
        )

    def post(self, request, rating):
        return redirect(reverse('thanks'))


class ThankView(View):
    template = 'thanks.html'

    def get(self, request):
        return render(
            request,
            self.template
        )
