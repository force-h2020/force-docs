Starting the Workflow Manager
=============================

The Workflow Manager can be started from within the ``edm`` environment with,

.. code-block:: console

    (edm)$ edm run -e force-pyXX -- force_wfmanager

Alternatively one can enter the ``force-pyXX`` environment,

.. code-block:: console

    (edm)$ edm shell -e force-pyXX

and then,

.. code-block:: console

    (force-pyXX)(edm)$ force_wfmanager

Views
-----

The Workflow Manager has two major UI components or "views":

``Setup Workflow``
    For constructing the workflow, selecting parameters and KPIs and selecting
    an optimizer.

.. figure:: images/setup_view.png
    :align: center
    :scale: 60 %

``View Results``
    For viewing the results of an optimization.

.. figure:: images/results_view.png
    :align: center
    :scale: 60 %

You can switch between the views with the top-left button in the tool-bar: the label
of this button will change accordingly. We will consider the two views, in turn, over the
next two topics.
