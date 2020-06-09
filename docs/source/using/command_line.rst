Using the Command Line
======================

Both the BDSS and the Workflow Manager can be invoked from the command line whilst
running a bash shell in the  ``force-py36`` Enthought Deployment Manager (EDM)
environment.

.. code-block:: console

    # enter a shell running the environment
    $ edm shell -e force-py36

    # execute the workflow
    (force-py36)$ force_bdss workflow.json

    # open the Workflow Manager with the workflow loaded
    (force-py36)$ force_wfmanager workflow.json

    # open the Workflow Manager
    (force-py36)$ force_wfmanager

The ``force_bdss`` command initiates the BDSS MCO runner, and therefore must be passeda workflow JSON
that contains optimization instructions. The ``force_wfmanager`` command initiates the Workflow Manager
GUI, and therefore can start up with a default empty workflow, since it provides additional UI features to
create, modify and export workflows.
The ``force_bdss`` can also be invoked using the ``--evaluate`` flag, which switches the application from
'optimize' to 'evaluate' mode and performs a single point evaluation of the workflow only. This functionality
was designed to allow an external process (or program) to control the optimization procedure, whilst the
system itself continues to be represented as a FORCE BDSS workflow. This is considered an 'advanced'
feature of the BDSS framework, and so will be explored in a later extension to the main tutorial.
EDM also supports running commands from outside a shell, using the ``edm run`` command.

.. code-block:: console

    $ edm run -e force-py36 -- force_wfmanager

For further assistance on EDM, use the ``edm --help`` tool or visit the
`latest documentation <https://docs.enthought.com/edm/>`_.
