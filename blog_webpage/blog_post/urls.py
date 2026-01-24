from . import views
from django.urls import path
urlpatterns = [
    path('',views.home, name='home'),
    path('forms',views.Create_Post,name='Create_Post'),
]