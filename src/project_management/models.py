from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime


class Team(models.Model):
    name = models.CharField(max_length=50)
    date_created = models.DateField(default=datetime.datetime.now)

    def __str__(self) -> str:
        return self.name

class Employee(AbstractUser):

    team = models.ManyToManyField(Team,through='Members', related_name='members') #Para que el modelo Team tenga acceso a los miembros del equipo related_name siempre ira donde sale el ManyToManyField

    def __str__(self) -> str:
        return f'{self.username}'

    class Meta:
        verbose_name = 'Employee'
        verbose_name_plural = 'Employees'


class ProjectManager(Employee):
    salary = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        ordering = ['username',]
        db_table = 'project_manager'


class Programmer(Employee):
    salary = models.DecimalField(decimal_places=2, max_digits=10)
    class Meta:
        ordering = ['username',]
        db_table = 'programmer'



class Members(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_members')
    programmer = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='team_programmer')

    def __str__(self) -> str:
        return self.programmer.username

class Client(models.Model):
    name = models.CharField(max_length=60, unique=True)
    date_joined = models.DateField(default=datetime.datetime.now)

    class Meta:
        db_table = 'client'

    def __str__(self) -> str:
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=60, unique=True)
    description = models.CharField(max_length=60, unique=True)
    date_created = models.DateField(default=datetime.datetime.now)
    slug = models.SlugField(max_length=255)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name='clients_projects')
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_project')

    class Meta:
        ordering = ['name', 'description']
        db_table = 'project'

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=60, unique=True)
    date_start = models.DateField(auto_now=True)
    date_end = models.DateField(auto_now=True)
    is_finished = models.BooleanField(default=False)
    project = models.ForeignKey(
        Project, on_delete=models.DO_NOTHING, related_name='tasks')
    assigned_to = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='employee_tasks')
    slug = models.SlugField(max_length=255)

    class Meta:
        db_table = 'task'
        ordering = ['title', 'date_start', 'date_end']
        

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(
        Employee, on_delete=models.DO_NOTHING, related_name='comment_user')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comment_tasks')
    text = models.CharField(max_length=400)
    published_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['published_date']

    def __str__(self) -> str:
        return self.text
