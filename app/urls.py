from django.contrib import admin
from django.urls import path
from genres.views import GenreCreatListView, GenreRetriveUpdateDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreatListView.as_view(), name='genre-create-list-view'),
    path('genres/<int:pk>/', GenreRetriveUpdateDestroy.as_view(), name='genre-detail-view'),
]
