from django.contrib import admin
from .models import Task, ExtraFieldForTask, TypeField

admin.site.register(Task)
admin.site.register(ExtraFieldForTask)
admin.site.register(TypeField)
