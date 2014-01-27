try:
    from django.utils.timezone import now
except ImportError:
    import datetime
    now = datetime.datetime.now

from django.db import models
from django.db.models.query import QuerySet


class BroadcastManager(models.Manager):
    """
    Manager class to show only active broadcast messages
    """
    class BroadcastQuerySet(QuerySet):
        def for_unauth_users(self):
            return self.exclude(user_target=self.model.TARGET_AUTHENTICATED)

        def for_auth_users(self):
            return self.exclude(user_target=self.model.TARGET_UNAUTHENTICATED)

    def get_query_set(self):
        return self.BroadcastQuerySet(self.model)

    def active(self):
        """Return only active messages"""
        return super(BroadcastManager, self).filter(is_published=True)

    def current(self):
        """Return only current and active messages"""
        current_time = now()
        return self.active().filter(end_time__gte=current_time).filter(
            start_time__lte=current_time)

    def latest(self):
        """Return the broadcast message to display"""
        try:
            return self.current().order_by("end_time")[0]
        except IndexError:
            return None
