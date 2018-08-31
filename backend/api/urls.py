
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('sentences', views.sentences, name='fetch_sentences')
]