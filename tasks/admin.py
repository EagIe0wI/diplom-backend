from django.contrib import admin
from .models import Task, ExtraTaskField, TypeField

admin.site.register(Task)
admin.site.register(ExtraTaskField)
admin.site.register(TypeField)
