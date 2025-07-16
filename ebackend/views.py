from django.shortcuts import render
from django.http import HttpResponse
def home (request):

    # return HttpResponse("Welcome to the home page!")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("This is the about page.")

def contact(request):
    return HttpResponse("This is the contact page.")