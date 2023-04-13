from django.shortcuts import render
from django.http import HttpResponse
from .models import Person


def index(request):
    latest_Person_list = Person.objects.all()
    context = {
        'latest_Person_list': latest_Person_list,
    }
    return render(request, "SopApp/index.html", context)

def detail(request, Person_id):
    return HttpResponse("You're looking at Person %s." % Person_id)


def results(request, Person_id):
    response = "You're looking at the results of Person %s."
    return HttpResponse(response % Person_id)


def vote(request, Person_id):
    return HttpResponse("You're voting on Person %s." % Person_id)