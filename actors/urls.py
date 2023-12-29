from django.contrib import admin
from django.urls import path
from actors.views import ActorCreateListView, ActorRetriveUpdateDestroyView


urlpatterns = [
    # Actores
    path('actores/', ActorCreateListView.as_view(), name='actor-detail-view'),
    path('actores/<int:pk>/', ActorRetriveUpdateDestroyView.as_view(),
         name='actor-detail-view'),
]
