from django.http import HttpResponse
from django.shortcuts import render
from .models import Room
from .forms import RoomForm

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    print(rooms)
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, id):
    room = Room.objects.get(id=id)
    return render(request, 'base/room.html', {'room':room})

def createRoom(request):
    return render(request, 'base/room_form.html',{'form':RoomForm})