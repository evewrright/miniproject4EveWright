from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from .models import Task
from .forms import TaskForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin


class MyLoginView(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("todo:index")


class IndexView(LoginRequiredMixin, generic.ListView):
    model = Task
    template_name = "todo/index.html"
    context_object_name = "tasks"

    def get_queryset(self):
        # Only retrieve tasks that were created by current user
        if self.request.user.is_authenticated:
            return Task.objects.filter(created_by_id=self.request.user, complete=False)
        else:
            return Task.objects.none()

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = "todo/detail.html"
    context_object_name = "task"

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.created_by != self.request.user:
            return redirect('todo:index')
        return super().dispatch(request, *args, **kwargs)


class Create(LoginRequiredMixin, generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/create.html"

    success_url = reverse_lazy("todo:index")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class Update(LoginRequiredMixin, generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/update.html"
    #fields = ['title', 'description', 'category']
    success_url = reverse_lazy("todo:index")

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.created_by != self.request.user:
            return redirect('todo:index')
        return super().dispatch(request, *args, **kwargs)


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")
    template_name = "todo/index.html"


def mark_complete(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(pk=task_id)
        task.complete = True
        task.save()
        return HttpResponseRedirect(reverse('todo:index'))
