from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from task.models import Task, Tag


def index(request: HttpRequest) -> HttpResponse:
    num_tasks = Task.objects.count()
    num_tags = Tag.objects.count()

    context = {
        "num_tasks": num_tasks,
        "num_tags": num_tags,
    }
    return render(request, "task/index.html", context=context)


class TagListView(ListView):
    model = Tag
