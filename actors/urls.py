from django.contrib import admin
from django.urls import path
from actors.views import ActorCreateListView, ActorRetriveUpdateDestroyView


urlpatterns = [
    # Actores
    path('actors/', ActorCreateListView.as_view(), name='actor-detail-view'),
    path('actors/<int:pk>/', ActorRetriveUpdateDestroyView.as_view(),
         name='actor-detail-view'),
]
