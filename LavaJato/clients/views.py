from django.shortcuts import render
from django.http import HttpResponse


def clients(req):
    return render(req, 'clients.html')
