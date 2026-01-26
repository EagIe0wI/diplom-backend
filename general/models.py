from django.db import models

# Create your models here.

# User (login, password, tasks, tags)
# Пользователь (Логин, Пароль, Задачи, Тэги)
class User(models.Model):
    login = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.login.title()}"

# Task (name, description, deadline, repeatable, tags)
# Задача (Название, Дедлайн, Повторяемость, Описание, Теги)
class Task(models.Model):
    user_id = models.ForeignKey(
        'User',
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

# Tag (name, description, deadline, repeatable)
# Тэг (Название, Описание, Дедлайн, Повторяемость)
class Tag(models.Model):
    user_id = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=225)
    deadline = models.DateField()
    repeatable = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name.title()}"

# Event (name, description, date)
# Событие (Название, Описание, Дата)
class Event(models.Model):
    user_id = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=225)
    date = models.DateField()

    def __str__(self):
        return f"{self.name.title()}"

# Extra (task_id, key, value, typeOfValue)
# Екстра-поле (ссылка на Task, наименование поля, содержимое поля, тип содержимого)
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

# TypeField (value, displayName)
# Тип поля (техническое наименование, наименование для пользователя)
class TypeField(models.Model):
    value = models.CharField(max_length=50)
    displayName = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name.title()}"