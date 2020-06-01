User Interface
==============


Envisage Service Offers
-----------------------

A plugin can also define one or more custom visualization classes for the
GUI application ``force-wfmanager``, typically to either display data or
provide a tailor-made UI for a specific user. In which case, the plugin class
must inherit from ``force_bdss.core_plugins.service_offer_plugin.ServiceOfferExtensionPlugin``
, which is a child class of ``BaseExtensionPlugin``. Any UI subclasses
can then be made discoverable by ``force-wfmanager`` using the ``envisage``
``ServiceOffer`` protocol through the ``get_service_offer_factories`` method::

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

Make sure to import the module containing the data view class from inside
``get_service_offer_factories``: this ensures that running BDSS without a GUI
application doesn't import the graphical stack.

Custom UI classes
-----------------

There are currently two types of custom UI object that may be contributed by a
plugin: ``IBasePlot`` and ``IContributedUI``. These interfaces represent requirements
for any UI feature that can be used to display MCO data or a present a simplified
workflow builder respectively.

Also, multiple types of plugin
contributed UI objects can be imported in the same call. For instance::

    def get_service_offer_factories(self):
        from force_wfmanager.ui import IBasePlot, IContributedUI
        from .example_custom_uis import PlotUI, ExperimentUI, AnalysisUI

        return [
            (IBasePlot, [PlotUI]),
            (IContributedUI, [ExperimentUI, AnalysisUI])
        ]
