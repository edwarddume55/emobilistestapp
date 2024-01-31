from django.urls import path
from . import views

urlpatterns = [
    path('',views.inbox, name='index'),
    path('send-Message/',views.sendMessage, name='send-message'),
    path('editMessage/<str:pk>/',views.editMessage, name='edit-Message'),
]