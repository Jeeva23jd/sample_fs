from django.urls import path
from . import views

urlpatterns=[
    path('',views.focus,name='focus'),
    path('in/',views.sample,name='sample'),
    path('new/',views.sample1,name='sample1'),
]