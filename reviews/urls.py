from django.contrib import admin
from django.urls import path
from reviews.views import ReviewCreateListView, ReviewRetriveUpdateDestroy

urlpatterns = [ 
    # Reviews
    path('reviews/', ReviewCreateListView.as_view(), name='review-detail-view'),
    path('reviews/<int:pk>/', ReviewRetriveUpdateDestroy.as_view(),
         name='review-detail-view'),
]
