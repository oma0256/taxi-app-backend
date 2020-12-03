from django.contrib import admin

from trips.models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    fields = (
        'id', 'pick_up_address', 'updated',
        'status', 'created', 'drop_off_address',
    )
    list_display = (
        'id', 'pick_up_address', 'updated',
        'status', 'created', 'drop_off_address',
    )
    list_filter = ('status',)
    readonly_fields = ('id', 'created', 'updated',)
