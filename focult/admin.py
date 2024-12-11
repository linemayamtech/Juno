from django.contrib import admin
from .models import *

@admin.register(Computer)
class ComputerAdmin(admin.ModelAdmin):
    list_display = ('id', 'c_host_name', 'c_ip_address', 'c_system_status',
                    'c_operating_system', 'c_username', 'uuid', 'c_log_ts')
    list_filter = ('c_system_status', 'c_operating_system')  # Filters in the sidebar
    search_fields = ('c_host_name', 'c_ip_address', 'uuid')  # Search bar

    def get_queryset(self, request):
        """Override to fetch all records from the Computer table."""
        return super().get_queryset(request).all()

admin.site.register(Organization)
admin.site.register(Employee)
# admin.site.register(Computer)

