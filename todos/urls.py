from django.urls import path
from todos.views import show_todo_list, todo_list

urlpatterns = [
    path("", todo_list, name="todo_list_list"),
    path("<int:id>/", show_todo_list, name="todo_list_detail"),
]
