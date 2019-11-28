from django.urls import path
from Store.views import *
urlpatterns = [
    path('login/',login)
]