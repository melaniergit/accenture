from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Teste A P A R E C E T E S T E A P A R E C E ")
