=================
django-broadcasts
=================

This version of Django Site Broadcasts was forked to provide a way to schedule client-side messages:

    * Across the whole site or on specific pages
    * For a specified amount of time
    * Uses a cookie to mark that the message was shown
    * For all users, authenticated users only, or unauthenticated users only
    * Retrievable via AJAX to allow for page caching
    * Django 1.5+ compatibility

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

#. Add this line to your ``urls.py``::

    url(r'^messages/', include('broadcasts.urls')),


Usage
=====

If you have this in your HTML somewhere::

    <div id="messages"></div>

you can use this simple jQuery snippet to retrieve all available broadcasts::

    <script type="text/javascript" src="http://code.jquery.com/jquery-1.10.2.min.js"></script>
    <script type="text/javascript">
        function addMessage(message) {
            $('#messages').append('<div class="alert">' + message + '</div>');
        };
        $.getJSON("{% url 'broadcast_messages' %}", function(data){
            $.each(data, function(index, value) {addMessage(value.message)});
        });
    </script>

