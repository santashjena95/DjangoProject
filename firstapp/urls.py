from django.urls import path
from . import views
urlpatterns = [
    path('add', views.add, name='add'),
    path('result', views.result, name='result'),
    path('checking', views.checking, name='second-page'),
    path('tweet', views.tweet, name='tweet'),
    path('twt_res', views.twt_res, name='twt_res'),
    #path('sort', views.sort, name='sort'),
]