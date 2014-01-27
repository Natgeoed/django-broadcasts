from django.conf import settings

DEFAULT_SETTINGS = {
    'MESSAGE_TYPE_CHOICES': []
}
USER_SETTINGS = DEFAULT_SETTINGS.copy()
USER_SETTINGS.update(getattr(settings, 'BROADCAST_SETTINGS', {}))

globals().update(USER_SETTINGS)
