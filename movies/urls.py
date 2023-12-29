from django.contrib import admin
from django.urls import path
from movies.views import MovieCreateListView, MovieRetriveUpdateDestroy

urlpatterns = [    
    # Movies
    path('movies/', MovieCreateListView.as_view(), name='movie-detail-view'),
    path('movies/<int:pk>/', MovieRetriveUpdateDestroy.as_view(),
         name='movie-detail-view'),

]
