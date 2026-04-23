from django.db import models

class Task(models.Model):
    user_id = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=225)
    deadline = models.DateField()
    repeatable = models.CharField(max_length=50)
    tags = models.ForeignKey(
        "Tag",
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"{self.name.title()}"

class ExtraTaskField(models.Model):
    task_id = models.ForeignKey(
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
        return f"{self.name.title()}"
