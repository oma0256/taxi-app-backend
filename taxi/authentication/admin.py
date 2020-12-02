from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from authentication.models import User


class UserAdmin(BaseUserAdmin):
    pass


# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
