from extra_views import InlineFormSetFactory
from .models import Task, Project

class TaskFormSet (InlineFormSetFactory):
    model = Task
    fields = ['title', 'description', 'assigned_to']
    factory_kwargs = {'extra': 2, 'max_num': None,
                      'can_order': False, 'can_delete': False}