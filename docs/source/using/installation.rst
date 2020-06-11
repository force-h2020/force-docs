Installation
============

The FORCE 2020 Repositories
---------------------------

The BDSS, the Workflow Manager and all plugins can be cloned from the
`Force 2020 github respositories <https://github.com/force-h2020>`_.
For the BDSS and Workflow Manager,

.. code-block:: console

    git clone https://github.com/force-h2020/force-bdss
    git clone https://github.com/force-h2020/force-wfmanager

This tutorial uses the Enthought-Example and Nevergrad plugins as examples,

.. code-block:: console

    git clone https://github.com/force-h2020/force-bdss-plugin-enthought-example
    git clone https://github.com/force-h2020/force-bdss-plugin-nevergrad


Enthought Deployment Manager
----------------------------

The BDSS, the Workflow Manager and plugins must be installed through the `Enthought Deployment
Manager (EDM) <https://www.enthought.com/enthought-deployment-manager/>`_, an environment and
package manager similar to Anaconda. EDM's documentation is
`here <http://docs.enthought.com/edm/>`_.

To install EDM, follow the instructions specific to your operating system
`here <https://docs.enthought.com/edm/installation.html>`_.

Once EDM is installed enter the EDM shell,

.. code-block:: console

    edm shell

and install the default environment,

.. code-block:: console

    edm install -y click setuptools

You in the default environment called ``edm`` and your shell prompt contains ``(edm)``.

Repository Installation
-----------------------

The default is the 'bootstrap' environment, used to install the cloned respositories.
For each respository in turn, cd into its directory and then install it with
``python -m ci install``. i.e.,

.. code-block:: console

    ~/Force-Project/force-bdss (edm)$ python -m ci install

    ~/Force-Project/force-bdss (edm)$ cd ../force-wfmanager
    ~/Force-Project/force-wfmanager (edm)$ python -m ci install

    ~/Force-Project/force-wfmanager (edm)$ cd ../force-bdss-plugin-enthought-example
    ~/Force-Project/force-bdss-plugin-enthought-example (edm)$ python -m ci install

    ~/Force-Project/force-wfmanager (edm)$ cd ../force-bdss-plugin-nevergrad
    ~/Force-Project/force-bdss-plugin-nevergrad (edm)$ python -m ci install

    ...etc

The BDSS Runtime Environment
----------------------------

.. _bdss-environment-ref:

BDSS must be run in a separate environment from the default. To create this environment, first cd
into the cloned force-bdss respository,

.. code-block:: console

    ~/Force-Project (edm)$ cd force-bdss

and then,

.. code-block:: console

    ~/Force-Project/force-bdss (edm)$ python -m ci build-env

This creates a environment called ``force-pyXX``, where ``XX`` refers to the python version that
the environment runs. You will see this in the list of EDM environments,

.. code-block:: console

    edm environments list

    >> * edm           cpython  3.6.9+2  win_x86_64  msvc2015  ~\.edm\envs\edm
    >>   force-pyXX    cpython  3.6.9+2  win_x86_64  msvc2015  ~.edm\envs\force-pyXX

To run BDSS from the command line see :ref:`Using the Command Line <cli-ref>`.




