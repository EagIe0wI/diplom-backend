from django.db import models
from tags.models import Tag

class Task(models.Model):
    user = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=225)
    deadline = models.DateField(null=True, blank=True, default=None)
    repeatable = models.CharField(max_length=50)
    tag = models.ForeignKey(
        'tags.Tag',
        on_delete=models.PROTECT,
        default=None
    )

    def __str__(self):
        return f"{self.name.title()}"

class ExtraTaskField(models.Model):
    task = models.ForeignKey(
        "Task",
        on_delete=models.CASCADE,
    )
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=225)
    typeOfValue = models.ForeignKey(
        "TypeField",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"{self.task_id} {self.key}"

class TypeField(models.Model):
    value = models.CharField(max_length=50)
    displayName = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.displayName.title()}"
