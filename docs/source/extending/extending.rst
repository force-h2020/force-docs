Extending the BDSS: Plugin Development
======================================

Force BDSS is extensible through the `Envisage <https://docs.enthought.com/envisage/index.html>`_
plugin framework. A plugin can be (and generally is) provided as a separate python package that
provides some new classes. Force BDSS will find these classes from the plugin at startup.

A single plugin can provide one or more of the following: ``MCO``, ``DataSources`` or ``NotificationListeners``.
It can optionally provide ``DataView`` and ``ContributedUI`` objects to be used by the ``force_wfmanager`` GUI: these
features will be dealt with in an extension tutorial.


An example plugin implementation is available at:

https://github.com/force-h2020/force-bdss-plugin-enthought-example

To implement a new plugin, you must define at least four classes:

- The ``Plugin`` class itself.
- One of the entities you want to implement: a ``DataSource``,
  ``NotificationListener`` or ``MCO``.
- A ``Factory`` class for the entity above: it is responsible for creating the
  specific entity, for example, a ``DataSource``
- A ``Model`` class which contains configuration options for the entity.
  For example, it can contain login and password information so that its data
  source knows how to connect to a service. The ``Model`` is also shown visually
  in the ``force_wfmanager`` UI, so some visual aspects need to be configured as
  well.

.. topic:: Topics

    .. toctree::
       :maxdepth: 2

        Traits and TraitsUI <traits>
        The Plugin <create_install>
        Factories and Classes <factory_class>
        Data Source <data_source>
        Parameterization <parameter>
        Optimizer <optimizer_engine>
        Notification <notification>
        User Interface <ui>
