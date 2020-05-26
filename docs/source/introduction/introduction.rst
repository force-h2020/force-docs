Introduction
============

The business decision support system (BDSS) is a software for optimization of industrial processes
in terms of economic and material constraints. It has been developed under the aegis of the
`Formulations and Computational Engineering <https://www.the-force-project.eu/>`_ (FORCE) project
of the `European Materials Modelling Council <https://emmc.info/>`_ (EMMC). The EMMC is a consortium
of academic and industrial partners spread across Europe,
with the mission of "the integration of materials modelling and digitalization critical for more
agile and sustainable product development."

More specifically the BDSS is a software for single- and multiple-criterion optimization of a directed
graph of computational operations (functions). The functions might include molecular-dynamics
or computational fluid dynamics simulations, interpolation of experimental data and economic cost-price
calculations. Nevertheless the BDSS is a general optimization software: the functions can be anything.

The BDSS can be run either as a stand-alone command-line program or within a graphic user interface (GUI)
software called the **Workflow Manager**. The BDSS is also extensible: "plugins" can be developed by the user
that add functionality to the software, typically in terms of functions and optimization algorithms.

.. topic:: Topics

    .. toctree::
       :maxdepth: 2

        Optimization <optimization>
