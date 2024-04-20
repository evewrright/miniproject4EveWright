from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Task
from django.urls import reverse_lazy

class IndexView(generic.ListView):
    model = Task
    template_name = "todo/index.html"
    context_object_name = "tasks"


class DetailView(generic.DetailView):
    model = Task
    template_name = "todo/detail.html"
    context_object_name = "task"


class Create(generic.CreateView):
    model = Task
    template_name = "todo/create.html"
    fields = ['title', 'description', 'category']
    success_url = reverse_lazy("todo:index")

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Set the created_by field
        return super().form_valid(form)


class Update(generic.UpdateView):
    model = Task
    template_name = "todo/update.html"
    fields = ['title', 'description', 'category']
    success_url = reverse_lazy("todo:index")
