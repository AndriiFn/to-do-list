from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:
    tasks = Task.objects.all()
    num_tasks = Task.objects.count()
    num_tags = Tag.objects.count()

    context = {
        "num_tasks": num_tasks,
        "num_tags": num_tags,
        "tasks": tasks,
    }
    return render(request, "task/index.html", context=context)


class TagListView(ListView):
    model = Tag


class TagCreateView(CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("task:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tag-list")


class TaskCreateView(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:index")


class TaskUpdateView(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("task:index")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("task:index")
