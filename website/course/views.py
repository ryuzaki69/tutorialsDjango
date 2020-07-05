from django.http import HttpResponse
from django.shortcuts import render


def show(request) :
    return HttpResponse('<div> <row>hello, </row> <row>world !!!</row> </div>')
