from django.contrib import admin
from catalog.models import *

# admin.site.register(User)
admin.site.register(Categorise)
admin.site.register(Application)


class UserAdmin(admin.ModelAdmin):
    list_display = ( 'username', 'email', 'role')
    fields = ('name', 'surname', 'username', 'email', 'password', 'role')

admin.site.register(User, UserAdmin)
