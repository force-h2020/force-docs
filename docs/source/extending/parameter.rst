Parameterization
================

MCO parameter types also require a model and a factory per each type. Right
now, the only typo encountered is Range, but others may be provided in the
future, by MCOs that support them.

The parameter factory must inherit from ``BaseMCOParameterFactory`` and
reimplement::

    def get_identifier(self):
    def get_name(self):
    def get_description(self):

as in the case of data source. Then::

    def get_model_class(self):

must return a model class for the given parameter, inheriting from
``BaseMCOParameter``. This model contains the data the user can set, and is
relevant to the given parameter. For example, in the case of a Range, it might
specify the min and max value, as well as the starting value.