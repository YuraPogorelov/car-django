from django.urls import path

from . import views

urlpatterns = [
    path('', views.CharacteristicsView.as_view()),
]