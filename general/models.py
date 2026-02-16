from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

# CustomUser (username, passwor)
# Пользователь (Логин, Пароль)
class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    password_hash = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return f"{self.username.title()}"

# Task (user_id, name, description, deadline, repeatable, tags)
# Задача (Ссылка на пользователя, Название, Дедлайн, Повторяемость, Описание, Теги)
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

# Tag (user_id, name, description, deadline, repeatable)
# Тэг (Ссылка на пользователя, Название, Описание, Дедлайн, Повторяемость)
class Tag(models.Model):
    user_id = models.ForeignKey(
        'CustomUser',
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=225)
    deadline = models.DateField()
    repeatable = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name.title()}"

# Event (user_id, name, description, date)
# Событие (Ссылка на пользователя, Название, Описание, Дата)
class Event(models.Model):
    user_id = models.ForeignKey(
        'CustomUser',
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