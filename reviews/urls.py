from django.urls import path 
from .views import SubmitCodeReviewAPIView, CodeReviewListAPIView, CodeReviewDetailAPIView, CodeReviewUpdateAPIView, CodeReviewDeleteAPIView

urlpatterns = [
    path("submitreview/",SubmitCodeReviewAPIView.as_view(),name="submit-review"),
    path('reviewlist/', CodeReviewListAPIView.as_view(),name="reviews"),
    path('singlereview/<int:pk>/', CodeReviewDetailAPIView.as_view(),name="review-detail"),
    path('updatereview/<int:pk>/', CodeReviewUpdateAPIView.as_view(),name="update-review"),
    path('deletereview/<int:pk>/',CodeReviewDeleteAPIView.as_view(),name="delete-review"),
]

