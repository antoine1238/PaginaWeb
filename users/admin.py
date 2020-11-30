from django.contrib import admin

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Local
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "user",
        "phone",
        "biography",
        "birthdate",
        "nationality",
        "picture",
    )
    

class ProfileInline(admin.StackedInline):

    model = Profile
    can_delete = False
    verbose_name_pural = "Profiles"

class UserAdmin(BaseUserAdmin):
    
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

admin.site.register(Profile, ProfileAdmin)

