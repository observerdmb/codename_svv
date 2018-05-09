from django.contrib import admin
from .models import Person
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


class PersonInLine(admin.StackedInline):
    model = Person
    can_delete = False
    verbose_name_plural = 'Persons'


class UserAdmin(BaseUserAdmin):
    inlines = (PersonInLine, )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
