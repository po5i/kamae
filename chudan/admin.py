from django.contrib import admin
from chudan.models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    #inlines = (UserStatInline, ) #django does not support nested inlines
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(UserAdmin):
    inlines = (ProfileInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin) 

# Register your models here.
admin.site.register(Status)
admin.site.register(Attendance)
admin.site.register(Rank)
admin.site.register(Championship)
admin.site.register(Travel)