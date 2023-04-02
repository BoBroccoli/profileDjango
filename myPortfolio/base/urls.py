from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('room/<int:id>', views.room),
    path('create-room/', views.createRoom),

]
