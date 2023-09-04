from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('', views.showChat, name="Show chat"),
    path('messages/send', views.sendMessage, name="Send Message"),
    path('messages/<int:receiver_id>/', views.getAllMessageByReceiverId, name='get_receiver_messages'),
]
