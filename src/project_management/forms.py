from django import forms
from . import models


class ProjectForm(forms.ModelForm):

    class Meta:
        model = models.Project
        fields = ['name', 'description', 'client','team']


class ClientForm(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ['name']


class TaskForm(forms.ModelForm):

    class Meta:
        model = models.Task
        fields = ['title', 'description', 'assigned_to']

    
