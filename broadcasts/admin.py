from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from broadcasts.models import BroadcastMessage
from broadcasts.forms import BroadcastMessageForm
from broadcasts.settings import MESSAGE_CHOICES


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

    def formfield_for_dbfield(self, db_field, **kwargs):
        print kwargs
        fld = super(BroadcastAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'message_type' and MESSAGE_CHOICES:
            fld.widget.choices = MESSAGE_CHOICES
        return fld

admin.site.register(BroadcastMessage, BroadcastAdmin)
