Creating a Plugin
=================

All plugin classes must

- Inherit from ``force_bdss.api.BaseExtensionPlugin``

.. code-block:: python

    from force_bdss.api import BaseExtensionPlugin, plugin_id

    VERSION = 0

    class ExamplePlugin(BaseExtensionPlugin):
    """This is an example of the plugin system for the BDSS."""

- Implement a ``id`` class member, that must be set to the result of
  calling the function ``plugin_id()``

.. code-block:: python

    id = plugin_id("enthought", "example", VERSION)

  The three arguments determine the unique name of the extension point

- Implement the methods ``get_name()``, ``get_version()`` and
  ``get_description()`` to return appropriate values. The ``get_version()``
  method in particular should return the same value as in the id (in this case
  zero). It is advised to extract this value in a global, module level
  constant

.. code-block:: python

    def get_name(self):
        return "Enthought example"

    def get_description(self):
        return "An example plugin from Enthought"

    def get_version(self):
        return VERSION

- Implement a method ``get_factory_classes()`` returning a list of all
  the classes (NOT the instances) of the entities you want to export.

.. code-block:: python

    def get_factory_classes(self):
        return [
            ExampleDataSourceFactory,
            ExampleMCOFactory,
            ExampleNotificationListenerFactory,
            ExampleUIHooksFactory,
        ]


Install the Plugin
------------------

In order for the BDSS to recognize the plugin, it must be installed as a package in the deployed
environment (``force-py36``). This can be performed using ``pip`` and an appropriate ``setup.py`` file,
that employs the ``setuptools`` package. Additional documentation describing package building using ``setuptools``
can be found `here <https://setuptools.readthedocs.io/en/latest/setuptools.html>`_.

The plugin is declared as an extension to the ``force_bdss`` by having it defined as the ``setup`` command
``entry_points`` keyword argument, under the namespace ``force.bdss.extensions``. You have to specify a path to the
plugin class (in this case ``ExamplePlugin``), as given below. The name (before the ``'='``) of the plugin is irrelevant, but to avoid confusion,
try to use the name of the module. For example

.. code-block:: python

    entry_points={
        "force.bdss.extensions": [
            "enthought_example = "
            "enthought_example.example_plugin:ExamplePlugin",
        ]
    }

A basic example ``setup.py`` file is therefore shown below

.. code-block:: python

    from setuptools import setup, find_packages

    VERSION = 0

    setup(
        name="enthought_example",
        version=VERSION,
        entry_points={
            "force.bdss.extensions": [
                "enthought_example = "
                "enthought_example.example_plugin:ExamplePlugin",
            ]
        },
        # Automatically looks for file directories containing __init__.py files
        # to be included in package
        packages=find_packages(),
    )

Running the following command line instruction from the same directory as ``setup.py`` will then install
the package in the deployed environment

.. code-block:: console

    edm run -e force-py36 -- pip install -e .

Advanced Plugins
----------------

Additionally, a plugin can also define one or more custom visualization classes for the
GUI application ``force-wfmanager``, typically to either display data or
provide a tailor-made UI for a specific user.

In which case, the plugin class
must inherit from ``force_bdss.api.ServiceOfferExtensionPlugin``
, which is a child class of ``BaseExtensionPlugin``. Any UI subclasses
can then be made discoverable by ``force-wfmanager`` using the Envisage
``ServiceOffer`` protocol through the ``get_service_offer_factories`` method

.. code-block:: python

    def get_service_offer_factories(self):
        """A method returning a list user-made objects to be provided by this
        plugin as envisage ServiceOffer objects. Each item in the outer list is
        a tuple containing an Interface trait to be used as the ServiceOffer
        protocol and an inner list of subclass factories to be instantiated
        from said protocol.

        Returns
        -------
        service_offer_factories: list of tuples
            List of objects to load, where each tuple takes the form
            (Interface, [HasTraits1, HasTraits2..]), defining a Traits
            Interface subclass and a list of HasTraits subclasses to be
            instantiated as an envisage ServiceOffer.
        """

Make sure to import the module containing the UI classes from inside
``get_service_offer_factories``: this ensures that running BDSS without a GUI
application doesn't import the graphical stack.

There are currently two types of custom UI object that may be contributed by a
plugin: ``IBasePlot`` and ``IContributedUI``. These interfaces represent requirements
for any UI feature that can be used to display MCO data or a present a simplified
workflow builder respectively.

Also, multiple types of plugin contributed UI objects can be imported in the same
method. For instance

.. code-block:: python

    from force_bdss.api import ServiceOfferExtensionPlugin

    class ExamplePlugin(ServiceOfferExtensionPlugin):
        """This is another example of the plugin system for the BDSS."""

        def get_service_offer_factories(self):
            from force_wfmanager.ui import IBasePlot, IContributedUI
            from .example_custom_uis import PlotUI, ExperimentUI, AnalysisUI

            return [
                (IBasePlot, [PlotUI]),
                (IContributedUI, [ExperimentUI, AnalysisUI])
            ]

These plugins are installed in the same way as described previously, but are only accessible when
running the ``force_wfmanager`` GUI.