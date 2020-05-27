Optimizer Engine
================

An optimizer engine


``BaseMCO``
-----------
eechuie ::

    class NevergradMCO(BaseMCO):

        def run(self, evaluator):
            model = evaluator.mco_model

            optim = NevergradMultiOptimizer(
                algorithms=model.algorithms,
                kpis=model.kpis,
                budget=model.budget)

            optimizer = AposterioriOptimizerEngine(
                kpis=model.kpis,
                parameters=model.parameters,
                single_point_evaluator=evaluator,
                verbose_run=model.verbose_run,
                optimizer=optim
            )

            for index, (optimal_point, optimal_kpis) \
                    in enumerate(optimizer.optimize()):
                model.notify_progress_event(
                    [DataValue(value=v) for v in optimal_point],
                    [DataValue(value=v) for v in optimal_kpis],
                )
``BaseMCOModel``
----------------
weygeygeyu::

    class NevergradMCOModel(BaseMCOModel):

        algorithms = Enum(
            *NevergradMultiOptimizer.class_traits()["algorithms"].handler.values
        )

        def default_traits_view(self):
            return View(
                Item("algorithms"),
                Item("budget", label="Allowed number of objective calls"),
                Item("verbose_run"),
            )

``IOptimizer``
--------------
ceygyug ::

    @provides(IOptimizer)
    class NevergradMultiOptimizer(HasStrictTraits):

        #: Algorithms available to work with
        algorithms = Enum(*ng.optimizers.registry.keys())

        #: A list of the output KPI parameters representing the objective(s)
        kpis = List(KPISpecification, visible=False, transient=True)

        def _algorithms_default(self):
            return "TwoPointsDE"

        def optimize_function(self, func, params):

            # Create instrumentation.
            instrumentation = translate_mco_to_ng(params)

            # Create optimizer.
            optimizer = ng.optimizers.registry[self.algorithms](
                parametrization=instrumentation,
                budget=self.budget
            )

            # Minimization/maximization specification
            minimize_objectives = ['MINI' in k.objective for k in self.kpis]

            # Create a multi-objective nevergrad function from
            # the MCO function.
            ng_func = partial(nevergrad_function,
                              function=func,
                              is_scalar=False,
                              minimize_objectives=minimize_objectives
                              )

            # Create a MultiobjectiveFunction object from that.
            ob_func = MultiobjectiveFunction(
                multiobjective_function=ng_func,
                upper_bounds=[k.scale_factor for k in self.kpis]
            )

            # Optimize. Ignore the return.
            optimizer.minimize(ob_func)

            # yield a member of the Pareto set.
            # x is a tuple - ((<vargs parameters>), {<kwargs parameters>})
            # return the vargs, translated into mco.
            for x in ob_func.pareto_front():
                yield translate_ng_to_mco(list(x[0]))

``BaseOptimizerEngine``
-----------------------
cebuehui ::

    class AposterioriOptimizerEngine(BaseOptimizerEngine):

        name = Str("APosteriori_Optimizer")

        optimizer = Instance(IOptimizer, transient=True)

        def optimize(self, *vargs):
            #: get pareto set
            for point in self.optimizer.optimize_function(
                    self._score,
                    self.parameters):
                kpis = self._score(point)
                yield point, kpis

        def unpacked_score(self, *unpacked_input):
            packed_input = list(unpacked_input)
            return self._score(packed_input)

``BaseMCOFactory``
------------------
eeygy ::

    class NevergradMCOFactory(BaseMCOFactory):

        def get_identifier(self):
            return "nevergrad_mco"

        def get_name(self):
            return "Gradient Free Multi Criteria optimizer"

        def get_model_class(self):
            return NevergradMCOModel

        def get_optimizer_class(self):
            return NevergradMCO

        def get_communicator_class(self):
            return BaseMCOCommunicator

        def get_parameter_factory_classes(self):
            return [
                FixedMCOParameterFactory,
                ListedMCOParameterFactory,
                RangedMCOParameterFactory,
                CategoricalMCOParameterFactory,
                RangedVectorMCOParameterFactory
            ]

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