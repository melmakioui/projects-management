from django.contrib import admin
from .models import *

# Register your models here.
models = (Employee, ProjectManager, Programmer, Client,
          Project, Task, Comment, Members, Team)

admin.site.register(models)