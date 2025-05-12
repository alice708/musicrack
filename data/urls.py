from django.urls import path

from . import views

urlpatterns = [
    #path("songs/", views.song, id="7zD7iZPRbfB0NSPuFNpkRH"),
    # Urls will start with data/ so /data/songs/id
    path("songs/<str:id>/", views.song)
]
