from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Task


class IndexView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    context_object_name = "tasks"


class DetailView(generic.DetailView):
    model = Task
    template_name = "todo/detail.html"
    context_object_name = "task"
