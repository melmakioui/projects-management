from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, DeleteView, UpdateView, CreateView
from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from . import forms
from .models import Project, Client, ProjectManager, Employee, Task, Programmer, Members
from extra_views import CreateWithInlinesView, UpdateWithInlinesView
from .formsets import TaskFormSet
from django.template.defaultfilters import slugify
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.

def test(request):
    return render(request,'website/base.html',{})


class Home(TemplateView):
    template_name = 'home.html'


class ListProjects(LoginRequiredMixin ,ListView):
    model = Project
    template_name = 'website/projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 10
    

class DetailProject(DetailView):
    model = Project
    template_name = 'website/projects/project_detail.html'


class CreateProject(CreateView):
    model = Project
    form_class = forms.ProjectForm
    template_name = 'website/projects/project_edit.html'
    success_url = reverse_lazy('project_list')

    def form_valid(self, form):
        name = form.instance.name
        form.instance.slug = slugify(name)
        form.save()
        return super().form_valid(form)
    

class UpdateProject(UpdateView):
    model = Project
    form_class = forms.ProjectForm
    template_name = 'website/projects/project_edit.html'

    def form_valid(self, form):
        name = form.instance.name
        form.instance.slug = slugify(name)
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy('project_detail', kwargs ={ 'slug': self.object.slug })
    

class DeleteProject(DeleteView):
    model = Project
    template_name = 'website/projects/project_delete_confirm.html'
    success_url = reverse_lazy('project_list')



class ListTask(ListView):
    model = Task
    template_name = 'website/tasks/task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        context['project'] = Project.objects.get(slug=slug)
        return context
    
    def get_queryset(self):
        slug = self.kwargs['slug']
        return Project.objects.get(slug=slug).tasks.all()
    

class DetailTask(DetailView): #One comments is finished
    model = Task
    template_name = 'website/tasks/task_detail.html'


class CreateTask(CreateView):
    model = Task
    form_class = forms.TaskForm
    template_name = 'website/tasks/task_edit.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['type'] = 'CREATE TASK'
        return context
    
    def get_form(self):
        form = super().get_form(self.form_class)
        slug = self.kwargs['slug']
        form.fields['assigned_to'].queryset = Project.objects.get(slug=slug).team.members.all()
        return form
    
    def form_valid(self, form):
        slug = self.kwargs['slug']
        form.instance.project = Project.objects.get(slug=slug)
        form.save()
        return super().form_valid(form)
    
    def get_success_url(self, **kwargs):
        return reverse_lazy('task_list', kwargs ={ 'slug': self.kwargs['slug'] })
    

class UpdateTask(UpdateView):
    model = Task
    form_class = forms.TaskForm
    template_name = 'website/tasks/task_edit.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['type'] = 'UPDATE TASK'
        return context

    def get_success_url(self, **kwargs):
        return reverse_lazy('task_list', kwargs ={ 'slug': self.kwargs['slug'] })


class DeleteTask(DeleteView):
    model = Task
    template_name = 'website/tasks/task_delete_confirm.html'

    def get_success_url(self, **kwargs) -> str:
        return reverse_lazy('project_detail', kwargs = {'slug': self.kwargs['slug']})
    




#FORMSETS

class CreateProjectWithTasks(CreateWithInlinesView):
    model = Project
    inlines = [TaskFormSet,]
    fields = ['name', 'description', 'client','team']
    template_name = 'website/projects/formsets/project_formset_edit.html'
    success_url = 'project_list'