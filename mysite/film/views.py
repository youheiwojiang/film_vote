from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mainpage(request):
	return HttpResponse("Welcome to the film site by Jimmy!")
