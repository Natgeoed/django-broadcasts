import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from broadcasts.managers import BroadcastManager
from broadcasts.settings import MESSAGE_TYPE_CHOICES


def one_year():
    return timezone.now() + datetime.timedelta(days=365)


class BroadcastMessage(models.Model):
    """
    A broadcast message to be displayed on the site.
    """
    TARGET_ALL = 1
    TARGET_AUTHENTICATED = 2
    TARGET_UNAUTHENTICATED = 3
    TARGET_CHOICES = (
        (TARGET_ALL, _('All users')),
        (TARGET_AUTHENTICATED, _('Anonymous or unauthenticated users only')),
        (TARGET_UNAUTHENTICATED, _('Authenticated users only')),
    )
    SHOW_ONCE = 1
    SHOW_ONCE_SESSION = 2
    SHOW_ALWAYS = 3
    SHOW_CHOICES = (
        (SHOW_ONCE, _("Show this message only once")),
        (SHOW_ONCE_SESSION, _("Show this message once per visit")),
        (SHOW_ALWAYS, _("Always show this message")),
    )
    user_target = models.IntegerField(
        _("user target"),
        choices=TARGET_CHOICES,
        default=TARGET_ALL)
    url_target = models.TextField(
        _("url target"),
        default=".*",
        help_text=_("""Uses regular expressions to match target URLs. <br/><br />
            Special Characters:<br />
            <code>"*"</code> is a wildcard, it matches anything.<br />
            <code>"|"</code> symbolizes an "OR" condition, either this or that.<br />
            <code>"$"</code> signifies a hard stop, matching paths must end at the "$".<br />
            <code>"?"</code> makes preceding character optional.<br /><br />
            Examples:<br />
            <code>.*</code> applies to entire site. <br/>
            <code>/path/to/this/$</code> matches that specific path only. <br/>
            <code>/path/to/this/$|/path/to/that$</code> matches either
            <code>/path/to/this/</code> OR <code>/path/to/that</code>
            <br/><code>/anything/beneath/this/</code> matches any path that starts with
            <code>/anything/beneath/this/</code><br />
            <code>/anything/here/?</code> matches any path starting with
            <code>/anything/here/</code> OR <code>/anything/here</code><br /><br />"""))
    title = models.CharField(
        _("title"),
        max_length=50,
        default="(No Title)")
    message = models.TextField(_("message"))
    start_time = models.DateTimeField(
        _("start time"),
        default=timezone.now, )
    end_time = models.DateTimeField(
        _("end time"),
        blank=True, null=True,
        default=one_year, )
    is_published = models.BooleanField(
        _("is published"),
        default=True, )
    show_frequency = models.IntegerField(
        _("show frequency"),
        choices=SHOW_CHOICES,
        default=SHOW_ONCE, )
    message_type = models.CharField(
        _("message type"),
        max_length=50,
        choices=MESSAGE_TYPE_CHOICES,
        blank=True,
        default="top-banner")
    creation_date = models.DateTimeField(
        _("creation date"),
        default=timezone.now,
        editable=False)

    objects = BroadcastManager()

    class Meta:
        ordering = ["-end_time"]

    def __str__(self):
        return "%s" % self.message[:15]

    def msg_info(self):
        return {
            'title': self.title,
            'message': self.message,
            'type': self.message_type,
            'frequency': {1: 'once', 2: 'session', 3: 'always'}[self.show_frequency],
        }
