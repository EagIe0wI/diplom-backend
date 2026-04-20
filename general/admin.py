from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Task, Tag, Event, ExtraTaskField, TypeField

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Task)
admin.site.register(Tag)
admin.site.register(Event)
admin.site.register(ExtraTaskField)
admin.site.register(TypeField)