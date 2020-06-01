Notification
============

Notification listeners are used to notify the state of the MCO to external
listeners, including the data that is obtained by the MCO as it performs the
evaluation. Communication to databases (for writing) and CSV/HDF5 writers are
notification listeners.

Each notification listener is defined by an implementation of ``BaseNotificationListenerFactory``, which
contributes both ``BaseNotificationListenerModel`` and  ``BaseNotificationListener``
subclasses. It therefore requires implementation of the following additional abstract methods alongside
the standard ``get_identifier``, ``get_name``, and ``get_description`` methods::

    def get_model_class(self):
        Returns a BaseNotificationListenerModel subclass

    def get_listener_class(self):
        Returns a BaseNotificationListener subclass

The BaseNotificationListener class must reimplement the following methods, that
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

