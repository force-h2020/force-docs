Data Sources
============

This is the "business end" of the data source, and where things are done.
The class must be derived from ``BaseDataSource``), and reimplement
the appropriate methods:

- ``run()``: where the actual computation takes place, given the
  configuration options specified in the model (which is received as an
  argument). It is strongly advised that the ``run()`` method is stateless.
- ``slots()``: must return a 2-tuple of tuples. Each tuple contains instances
  of the ``Slot`` class. Slots are the input and output entities of the
  data source. Given that this information depends on the
  configuration options, ``slots()`` accepts the model and must return the
  appropriate values according to the model options.
