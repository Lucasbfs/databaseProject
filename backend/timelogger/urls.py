from django.urls import path
from .views import UserListAPIView, ProjectListAPIView, TaskListAPIView, TimeLogListAPIView

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='user-list'),
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('tasks/', TaskListAPIView.as_view(), name='task-list'),
    path('timelogs/', TimeLogListAPIView.as_view(), name='timelog-list'),
]
