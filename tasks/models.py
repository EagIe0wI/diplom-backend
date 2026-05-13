from django.db import models

class Task(models.Model):
    STATUSES = {
        "todo": "Запланировано",
        "in_progress": "В процессе",
        "done": "Выполнено",
    }
    repeatables = {
        "none": "Не повторяется",
        "every_day": "Каждый день",
        "every_week": "Каждую неделю",
        "every_month": "Каждый месяц",
        "every_year": "Каждый год",
    }

    user = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=225, null=True, blank=True, default=None)
    deadline = models.DateField(null=True, blank=True, default=None)
    repeatable = models.CharField(max_length=11, choices=repeatables, default="none")
    tag = models.ForeignKey(
        'tags.Tag',
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        default=None
    )
    status = models.CharField(max_length=11, choices=STATUSES, default="todo")

    def __str__(self):
        return f"{self.name.title()}"

class ExtraFieldForTask(models.Model):
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
