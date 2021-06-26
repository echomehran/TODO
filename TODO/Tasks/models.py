from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):

    class State(models.TextChoices):
        My_Day = 'TD', 'Today'
        Important = 'IMP', 'Important'
        Planned = 'P', 'Planned'
        All = 'A', 'All'
        Completed = 'C', 'Completed'
        Tasks = 'T', 'Tasks'

    class Category(models.TextChoices):
        green = 'G', 'Green'
        yellow = 'Y', 'Yellow'
        red = 'R', 'Red'

    class Prioritize(models.TextChoices):
        A = 'A', 'THE_MOST_IMPORTANT'
        B = 'B', 'IMPORTANT'
        C = 'C', 'LESS_IMPORTANT'
        D = 'D', 'NOT_IMPORTANT_AT_ALL'

    title = models.CharField(max_length=300)
    description = models.TextField(blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True)
    repeat = models.DateTimeField(null=True, blank=True)
    state = models.CharField(
        max_length=3, choices=State.choices, default=State.Tasks)
    add_file = models.FileField(blank=True)
    add_step = models.CharField(max_length=5000, null=True, blank=True)
    user = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE)

    category = models.CharField(
        max_length=1, choices=Category.choices, blank=True, null=True)

    prioritize = models.CharField(
        max_length=2, choices=Prioritize.choices, blank=True, null=True)

    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:  # ! WARNING
        order_with_respect_to = 'user'


class NewList(models.Model):
    name = models.CharField(max_length=100)
    assigned_task = models.ForeignKey(
        Task, null=True, on_delete=models.CASCADE)
