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
The BDSS software will not be installed in this environment, but in a separate one. The following
commands however must be executed from the bootstrap environment.

Installation of the force BDSS runtime environment is performed with the
following command. This should be done from the directory containing the ``force-bdss`` folder (named
``Force-Project`` in this example)

.. code-block:: console

    ~/Force-Project (edm)$ cd force-bdss
    ~/Force-Project/force-bdss (edm)$ python -m ci build-env

This will create another edm environment called ``force-py36``.
Do not enter this environment. 

To install the BDSS

.. code-block:: console

    ~/Force-Project/force-bdss (edm)$ python -m ci install
    ~/Force-Project/force-bdss (edm)$ cd ..
    
To install the workflow manager

.. code-block:: console

    ~/Force-Project (edm)$ cd force-wfmanager
    ~/Force-Project/force-wfmanager (edm)$ python -m ci install
    ~/Force-Project/force-wfmanager (edm)$ cd ..

and (optional, but recommended), the example plugins

.. code-block:: console

    ~/Force-Project (edm)$ cd force-bdss-plugin-enthought-example
    ~/Force-Project/force-bdss-plugin-enthought-example (edm)$ python -m ci install
    ~/Force-Project/force-bdss-plugin-enthought-example (edm)$ cd ..





