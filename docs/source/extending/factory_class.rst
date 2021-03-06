Factories and Classes
---------------------
A factory object (``BaseFactory``) defines a set of other classes that are required to define
one of the following:

- a **data source**

- an **optimizer**

- a **parameterization**

- a **notifier**

Each factory returns the classes that are required. Both these and the factory class must be
written by the plugin writer. In turn, the former may depend on other classes that also
need to be written.

Below we provide links to well documented code examples of factories and their associated classes.

.. list-table:: Factories for different BDSS Categories
    :widths: 20 50 50 40 20
    :header-rows: 1

    * - BDSS category
      - factory
      - classes defined by factory
      - other classes
      - example

    * - data source
      - ``BaseDataSourceFactory``
      - ``BaseDataSource``, ``BaseDataSourceModel``
      -
      - `Gaussian <https://github.com/force-h2020/force-bdss-plugin-enthought-example>`_

    * - parameterization
      - ``BaseMCOParameterFactory``
      - ``BaseMCOParameter``
      -
      - `Ranged <https://github.com/force-h2020/force-bdss/blob/master/force_bdss/mco/parameters/mco_parameters.py>`_

    * - optimizer
      - ``BaseMCOFactory``
      - ``BaseMCO``, ``BaseMCOModel``, ``BaseMCOCommunicator``
      - ``BaseOptimizerEngine``, ``IOptimizer``
      - `Nevergrad <https://github.com/force-h2020/force-bdss-plugin-nevergrad/tree/master/force_nevergrad/mco>`_

In the following topics we go into these in more detail.
