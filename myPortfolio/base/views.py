from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Room
from .forms import RoomForm

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, id):
    room = Room.objects.get(id=id)
    return render(request, 'base/room.html', {'room':room})

def createRoom(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/room_form.html',{'form':RoomForm})

def updateRoom(request, id):
    room = Room.objects.get(id=id)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'base/room_form.html', {'form': form})