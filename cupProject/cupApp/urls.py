from django.urls import path
from . import views

# DIRECTING PATHS TO FUNCTIONS
urlpatterns = [
    path('cupIndex', views.cupIndex, name='cupindex'),
    path('changemat', views.changeMat, name='change'),
    path('createcup', views.createCup, name='create'),
    path('allcups/', views.allCups, name='allcups'),
    path('total/<int:number>', views.sumofAll, name='total'),
    path('hello/<str:name>', views.helloThere, name='hello'),
    path('times2/<int:number>', views.timesTwo, name='times2'),
    path('', views.index),
]