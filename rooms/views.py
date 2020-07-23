from django.shortcuts import render
from . import models
from datetime import datetime
from django.http import HttpResponse


def home(request):
    all_rooms = models.Room.objects.all()
    return render(request, "rooms/home.html", context={"rooms": all_rooms,})
    # return HttpResponse(content="<h1>hello</h1>")
