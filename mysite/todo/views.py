from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class MyLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "todo/index.html"
    context_object_name = "tasks"


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "todo/detail.html"
    context_object_name = "task"


class Create(LoginRequiredMixin, generic.CreateView):
    model = Task
    template_name = "todo/create.html"
    fields = ['title', 'description', 'category']
    success_url = reverse_lazy("todo:index")

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # Set the created_by field
        return super().form_valid(form)


class Update(LoginRequiredMixin, generic.UpdateView):
    model = Task
    template_name = "todo/update.html"
    fields = ['title', 'description', 'category']
    success_url = reverse_lazy("todo:index")
