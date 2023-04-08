
from django.urls import path
from . import views

urlpatterns = [


    # Projects
    path('', views.test, name='x'),

    path('projects/', views.ListProjects.as_view(), name='project_list'),

    path('project/new', views.CreateProject.as_view(), name='project_create'),

    path('project/<slug:slug>', views.DetailProject.as_view(), name='project_detail'),

    path('project/edit/<slug:slug>',
         views.UpdateProject.as_view(), name='project_update'),

    path('project/delete/<slug:slug>',
         views.DeleteProject.as_view(), name='project_delete'),

    # Tasks
    path('project/<slug:slug>/tasks/',
         views.ListTask.as_view(), name='task_list'),

    path('project/<slug:slug>/new/task',
         views.CreateTask.as_view(), name='task_create'),

    path('project/<slug:slug>/edit/task/<int:pk>',
         views.UpdateTask.as_view(), name='task_update'),

    path('project/<slug:slug>/delete/task/<int:pk>',
         views.DeleteTask.as_view(), name='task_delete'),


    # Project With Tasks

    path('project/new/tasks', views.CreateProjectWithTasks.as_view(),
         name='project_form_set')


]
