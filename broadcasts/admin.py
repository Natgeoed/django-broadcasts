from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from broadcasts.models import BroadcastMessage
from broadcasts.forms import BroadcastMessageForm


class BroadcastAdmin(admin.ModelAdmin):
    """Admin class for the broadcast messages"""
    form = BroadcastMessageForm
    list_display = (
        'title', 'user_target', 'show_frequency', 'start_time',
        'end_time', 'is_published')
    list_filter = ('is_published', 'show_frequency', 'user_target')
    search_fields = ['message', 'title']
    fieldsets = (
        (None, {
            'fields': ('title', 'message', 'message_type',)
        }),
        (_('Message Targeting'), {
            'fields': ('user_target', 'url_target')
        }),
        (_("Message Display"), {
            'description': _(
                "Messages will display only if they are published, "
                "it is between the start and end times, and the show "
                "frequency has not been exceeded."),
            'fields': ('show_frequency', 'is_published',
                      ('start_time', 'end_time'))
        })
    )

admin.site.register(BroadcastMessage, BroadcastAdmin)
