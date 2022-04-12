from django.urls import path
from .views import Detail_Todo, Create_Todo, Delete_Todo
from . import views

urlpatterns = [
    path('<int:pk>/', Detail_Todo.as_view()),
    path("tasks/", views.get_tasks),
    path("tasks/stats/", views.productivity_stats),
    path('create', Create_Todo.as_view()),
    path('delete/<int:pk>', Delete_Todo.as_view())
]