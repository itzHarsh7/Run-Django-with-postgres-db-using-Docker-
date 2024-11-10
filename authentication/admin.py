from django.contrib import admin
from .models import *
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User
        list_display = ['username', 'role', 'email', 'first_name', 'last_name']
class RoleAdmin(admin.ModelAdmin):
    class Meta:
        model = Role
        list_display = ['id', 'name', 'discription']
admin.site.register(User,UserAdmin)
admin.site.register(Role,RoleAdmin)
admin.site.register(Blog)