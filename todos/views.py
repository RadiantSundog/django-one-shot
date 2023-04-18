from django.shortcuts import render, get_object_or_404
from todos.models import TodoList

# Create your views here.


def show_todo_list(request, id):
    todo = get_object_or_404(TodoList, id=id)
    context = {
        "todo_list_object": todo,
    }
    return render(request, "recipes/detail.html", context)


def todo_list(request):
    todos = TodoList.objects.all()
    context = {"todo_list": todos}
    return render(request, "todos/list.html", context)
