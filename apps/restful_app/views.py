from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from models import *
from django.contrib import messages


def index(request):
    context = {
        "users" : User.objects.all()
    }
    return render(request, 'restful_app/index.html', context)

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if type(errors) == list:
        for error in errors:
            messages.error(request, error)
            return redirect('/new')
    else:
        newuser = User.objects.create(full_name=request.POST['full_name'], email=request.POST['email'])
        return redirect("/")

def new(request):
    return render(request, "restful_app/new.html")

def show(request, id):
    context = {
        "user" : User.objects.get(id=int(id))
    }
    return render(request, "restful_app/show.html", context)

def edit(request, id):
    context = {
        "user" : User.objects.get(id=int(id))
    }
    return render(request, "restful_app/edit.html", context)

def update(request, id):
    errors = User.objects.basic_validator(request.POST)
    if type(errors) == list:
        for error in errors:
            messages.error(request, error)
            return redirect('/new')
        else:
            User.objects.filter(id=int(id)).update(full_name=request.POST["full_name"], email=request.POST["email"])
            return redirect("/users/"+id)

def delete(request, id):
    User.objects.get(id=int(id)).delete()
    return redirect('/users')