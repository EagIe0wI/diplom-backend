from django.db import models

class Task(models.Model):
    STATUSES = {
        "todo": "Запланировано",
        "done": "Выполнено",
    }

    user = models.ForeignKey(
        'accounts.CustomUser',
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=225, null=True, blank=True, default=None)
    card = models.ForeignKey(
        'cards.Card',
        on_delete=models.CASCADE,
    )
    status = models.CharField(max_length=11, choices=STATUSES, default="todo")
    start_date = models.DateField(null=True, blank=True)
    rrule_rule = models.CharField(max_length=255, null=True, blank=True)


    def __str__(self):
        return f"{self.title.title()}"

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
