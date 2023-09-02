from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    # Send Message
    path('', views.getData, name='Api'),
]
