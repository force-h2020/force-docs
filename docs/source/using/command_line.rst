Using the Command Line
======================

Both the BDSS and the Workflow Manager can be envoked from the command line.

.. code-block:: console

    # execute the workflow
    $ edm run -e force-py36 -- force_bdss workflow.json

    # open the Workflow Manager with the workflow loaded
    $ edm run -e force-py36 -- force_wfmanager workflow.json

    # open the Workflow Manager
    $ edm run -e force-py36 -- force_wfmanager

Within the force-py36 environment of the Enthought Deployment Manager (EDM), the commands
are the same but without ``edm run -e`` at the start.

.. code-block:: console

    (force-py36)(edm)$ force_wfmanager
