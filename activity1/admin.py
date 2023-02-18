from django.contrib import admin
from .models import Profile


admin.site.site_header = "James Tito's Admin Page"


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_first_name', 'get_last_name', 'description')

    def get_first_name(self, obj):
        return obj.user.first_name
    get_first_name.short_description = 'First Name'

    def get_last_name(self, obj):
        return obj.user.last_name
    get_last_name.short_description = 'Last Name'

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False


admin.site.register(Profile, ProfileAdmin)
