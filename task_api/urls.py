from django.urls import path
from .views import TaskListCreate, TaskRetrieveUpdateDestroy #, mark_task_completed

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroy.as_view(), name='task-detail'),
]