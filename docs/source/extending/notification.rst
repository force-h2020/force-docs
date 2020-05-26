Notification
============

Notification listeners are used to notify the state of the MCO to external
listeners, including the data that is obtained by the MCO as it performs the
evaluation. Communication to databases (for writing) and CSV/HDF5 writers are
notification listeners.

The notification listener requires a model (inherit from
``BaseNotificationListenerModel``), a factory (from
``BaseNotificationListenerFactory``) and a notification listener
(from ``BaseNotificationListener``). The factory requires, in addition to::

    def get_identifier(self):
    def get_name(self):
    def get_description(self):
    def get_model_class(self):

the method::

    get_listener_class()
     return the notification listener object class.

The NotificationListener class must reimplement the following methods, that
are invoked in specific lifetime events of the BDSS::

    def initialize(self):
        Called once, when the BDSS is initialized. For example, to setup the
        connection to a database, or open a file.

    def finalize(self):
        Called once, when the BDSS is finalized. For example, to close the
        connection to a database, or close a file.

    def deliver(self, event):
        Called every time the MCO generates an event. The event will be passed
        as an argument. Depending on the argument, the listener implements
        appropriate action. The available events are in the api module.

