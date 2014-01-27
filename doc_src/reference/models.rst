===============
Model Reference
===============

BroadcastMessage
================

.. py:class:: BroadcastMessage

   .. py:attribute:: title

      **Required** ``CharField(50)``

      A title for the message. This attribute is passed to the client.

   .. py:attribute:: message

      **Required** ``TextField``

      The message. This attribute is passed to the client.

   .. py:attribute:: message_type

      ``CharField(50)``

      An arbitrary way to pass information to the client. You can define a set of choices via :ref:`MESSAGE_TYPE_CHOICES`\ . This attribute is passed to the client.
