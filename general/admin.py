from django.contrib import admin
from .models import User, Task, Tag, Event, ExtraTaskField, TypeField

# Register your models here.

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(ExtraTaskField)
admin.site.register(TypeField)