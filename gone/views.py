from django.shortcuts import render

from django.http import HttpResponse



def home(response):
    context = {"name":'siva'}
    return render(response,"home.html",context)

def about(response):
    context = {"name":'siva'}
    return render(response,"about.html",context)

def product(response):
    context = {"name":'siva'}
    return render(response,"product.html",context)