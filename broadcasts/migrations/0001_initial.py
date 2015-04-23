# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import broadcasts.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BroadcastMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_target', models.IntegerField(default=1, verbose_name='user target', choices=[(1, 'All users'), (2, 'Anonymous or unauthenticated users only'), (3, 'Authenticated users only')])),
                ('url_target', models.TextField(default=b'.*', help_text='Uses regular expressions to match target URLs. <br/>\n            <code>.*</code> applies to entire site. <br/>\n            <code>/path/to/this.html</code> matches that specific path. <br/>\n            <code>/path/to/this.html|/or/to/this.html</code> matches either\n            <code>/path/to/this.html</code> OR <code>/or/to/this.html</code>\n            <br/><code>/anything/under/.*</code> matches any path starting with\n            <code>/anything/under/</code>', verbose_name='url target')),
                ('title', models.CharField(default=b'(No Title)', max_length=50, verbose_name='title')),
                ('message', models.TextField(verbose_name='message')),
                ('start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='start time')),
                ('end_time', models.DateTimeField(default=broadcasts.models.one_year, null=True, verbose_name='end time', blank=True)),
                ('is_published', models.BooleanField(default=True, verbose_name='is published')),
                ('show_frequency', models.IntegerField(default=1, verbose_name='show frequency', choices=[(1, 'Show this message only once'), (2, 'Show this message once per visit'), (3, 'Always show this message')])),
                ('message_type', models.CharField(default=b'', max_length=50, verbose_name='message type', blank=True, choices=[(b'top-banner', b'Top-of-Page Banner')])),
                ('creation_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='creation date', editable=False)),
            ],
            options={
                'ordering': ['-end_time'],
            },
            bases=(models.Model,),
        ),
    ]
