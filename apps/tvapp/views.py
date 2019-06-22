from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from .models import *


def index(request):
    return HttpResponse("Hello")

def newshows(request):
    
    return render(request, 'tvapp/newshows.html')

def addshow(request):

    show = Show.objects.create(title = request.POST['title'], network = request.POST['network'], rldate = request.POST['rldate'], description = request.POST['description'])


    return redirect(f'/displayshow/{show.id}')


def displayshow(request, show_id):

    show = Show.objects.get(id=show_id)
    context = {
        "show": show
    }
    

    return render(request, 'tvapp/showconfirm.html', context)

def deleteshow(request, show_id):

    Show.objects.get(id=show_id).delete()

    # show = Show.objects.get(id=show_id)
    # show.delete()

    return redirect('/display')


def editshow(request, show_id):

    show = Show.objects.get(id=show_id)


    context = {

        "show": Show.objects.get(id=show_id),
    }

    return render(request, 'tvapp/editshow.html', context)


def process(request, show_id):

    show = Show.objects.get(id=show_id)
    show.title = request.POST['title']
    show.network = request.POST['network']
    show.rldate = request.POST['rldate']
    show.description = request.POST['comment']
    show.save()

    return redirect(f'/displayshow/{show_id}')

def display(request):

    context = {

        "all_shows": Show.objects.all()

    }

    return render(request, 'tvapp/display.html', context)




# Create your views here.
