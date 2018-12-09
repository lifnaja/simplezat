from django.urls import path

from .views import RatingView, CommentView ,ThankView



urlpatterns = [
	path('',RatingView.as_view(), name='ratings'),
	path('thanks/',ThankView.as_view(), name='thanks'),
	path('<str:rating>/',CommentView.as_view(), name='comment'),
]