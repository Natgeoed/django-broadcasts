===============
Getting Started
===============

Installation
============

#. Use ``pip`` to install the application:

   .. code-block:: bash

      $ pip install django-site-broadcasts

#. Then add ``broadcasts`` to your ``INSTALLED_APPS`` setting:

   .. code-block:: python

      INSTALLED_APPS = [
          # ...
          'broadcasts',
      ]


Configuration
=============

By default, message types are free form. You can define set choices in the settings:

   .. code-block:: python

      BROADCAST_SETTINGS = {
          'MESSAGE_CHOICES': [
             ('alert', 'Alert'),
             ('popup', 'Pop-up'),
             ('error', 'Error'),
          ]
      }

While you can define the ``MESSAGE_CHOICES`` at any time, any messages with a ``message_type`` value other than one of the choices will not appear selected in the admin form.