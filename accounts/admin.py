from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Doctor

# If you have custom fields on the CustomUser and want them to show up in the admin, you can customize the UserAdmin class here.
admin.site.register(CustomUser, UserAdmin)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'profession')
    search_fields = ('name', 'surname', 'profession')
    filter_horizontal = ('available_slots',)