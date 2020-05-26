Optimizer Engines
=================

The ``force_bdss.api`` package offers the ``BaseOptimizerEngine`` and
``SpaceSampler`` abstract classes, both of which are designed as utility objects for backend developers.

The ``BaseOptimizerEngine`` class provides a schema that can easily be reimplemented to
act as an interface between the BDSS and an external optimization library. Although it is not strictly
required to run an MCO, it is expected that a developer would import the object into a ``BaseMCO.run``
implementation, whilst providing any relevant pre and post processing of information for the specific used
case that the MCO is solving. The base class must simply define the following method::

    def optimize(self):

Which is expected to act as a generator, yielding values corresponding to optimised input parameters
and their corresponding KPIs. A concrete implementation of this base class, the ``WeightedOptimizerEngine``,
is provided that uses the ``SciPy`` library as a backend.

The ``SpaceSampler`` abstract class also acts as a utility class in order to sample
vectors of values from a given distribution. Implementations of this class could be used to either provide
trial parameter sets to feed into an optimiser as initial points, or importance weights to apply to each KPI.
The base class must define the following methods::

    def _get_sample_point(self):
    def generate_space_sample(self, *args, **kwargs):

Two concrete implementations of this class are provided: ``UniformSpaceSampler``, which performs a grid
search and ``DirichletSpaceSampler``, which samples random points from the Dirichlet distribution.

MCO Communicator
----------------

The MCO Communicator must reimplement BaseMCOCommunicator and two methods:
``receive_from_mco()`` and ``send_to_mco()``. These two methods can use files,
stdin/stdout or any other trick to send and receive data between the MCO and
the BDSS running as a subprocess of the MCO to evaluate a single point.