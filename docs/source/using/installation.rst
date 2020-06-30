Installation
============

To install both ``force-bdss`` and the ``force-wfmanager`` applications, first checkout the following
git repositories

.. code-block:: console

    git clone https://github.com/force-h2020/force-bdss
    git clone https://github.com/force-h2020/force-wfmanager
    git clone https://github.com/force-h2020/force-bdss-plugin-enthought-example

The last repository is optional, but recommended if you want to practice
writing plugins.

If you never installed the Enthought Deployment Manager (EDM), perform the following operations

.. code-block:: console

    wget https://package-data.enthought.com/edm/rh5_x86_64/1.11/edm_1.11.0_linux_x86_64.sh && bash ./edm_1.11.0_linux_x86_64.sh-b -f -p $HOME
    export PATH=${HOME}/edm/bin:${PATH}
    edm install --version 3.6 -y click setuptools
    edm shell

If you instead already have an EDM installation and a default environment, perform the following

.. code-block:: console

    edm shell
    edm install -y click setuptools

Verify that your shell prompt now contains the string "``(edm)``".
You are now in your default EDM environment, and we assume this environment to be the bootstrap environment.
Installation
============

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
Manager (EDM) <https://www.enthought.com/enthought-deployment-manager/>`_, a python
virtual environment and package manager. For new users it is worth examining EDM's
`documentation <http://docs.enthought.com/edm/>`_.

To install EDM, follow the instructions specific to your operating system
`,here <https://docs.enthought.com/edm/installation.html>`_.


The Bootstrap Environment
-------------------------

Once EDM is installed create a 'bootstrap' environment from which you can install
the BDSS, Workflow Manager and plugins,

.. code-block:: console

    edm install -e bootstrap -y click setuptools

Note that 'bootstrap' can be replaced by any name to the same effect. Now you can enter
``bootstrap`` with,

.. code-block:: console

    edm shell -e bootstrap

and your shell prompt is prefixed with ``(bootstrap)``.


The BDSS Runtime Environment
----------------------------

.. _bdss-environment-ref:

Although repositories (BDSS, etc) are installed *from* the ``bootstrap`` environment, they are
installed *into* a separate environment, within which the BDSS and the Workflow Manager will
actually run. Thus this environment has also to be created before installation. To do this
first cd into the cloned force-bdss respository,

.. code-block:: console

    ~/Force-Project (bootstrap)$ cd force-bdss

and then,

.. code-block:: console

    ~/Force-Project/force-bdss (bootstrap)$ python -m ci build-env

This creates a environment called ``force-pyXX``, where ``XX`` refers to the python version that
the environment runs (e.g. ``force-py36`` for python 3.6) . You will now see it in the list of EDM environments,

.. code-block:: console

    (bootstrap)$ edm environments list

    >> * bootstrap     cpython  3.6.9+2  win_x86_64  msvc2015  ~\.edm\envs\bootstrap
    >>   force-py36    cpython  3.6.9+2  win_x86_64  msvc2015  ~.edm\envs\force-pyXX

To run BDSS from the command line see :ref:`Using the Command Line <cli-ref>`.


Repository Installation
-----------------------

From the ``bootstrap`` environment (not ``force-pyXX``!), for each respository in turn,
cd into its directory and then install it with ``python -m ci install``. i.e.,

.. code-block:: console

    ~/Force-Project/force-bdss (bootstrap)$ python -m ci install

    ~/Force-Project/force-bdss (bootstrap)$ cd ../force-wfmanager
    ~/Force-Project/force-wfmanager (bootstrap)$ python -m ci install

    ~/Force-Project/force-wfmanager (bootstrap)$ cd ../force-bdss-plugin-enthought-example
    ~/Force-Project/force-bdss-plugin-enthought-example (edm)$ python -m ci install

    ~/Force-Project/force-wfmanager (bootstrap)$ cd ../force-bdss-plugin-nevergrad
    ~/Force-Project/force-bdss-plugin-nevergrad (bootstrap)$ python -m ci install

    ...etc
