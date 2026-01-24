from django.urls import path
from . import views

urlpatterns=[
    path('',views.httphome,name='httphome'),
    path('index/',views.display,name='display'),
    
]
