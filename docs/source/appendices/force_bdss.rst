BDSS Components
===============

Adapted from ....

Decision-making strategy
------------------------

The Force platform will be open and based on standards
such that all components (modelling, MCOs, KPIs, dataspaces, etc.) can seamlessly
exchange relevant information allowing an optimal business decision workflow to be
developed rapidly while the availability of cognitive elements in the user interfaces
will allow use even by non-experts in the materials modelling. Data from modelling
will be augmented with existing data including chemical and mechanical properties,
process characteristics, commercial and business data. In particular, information
on costs of raw and compound materials, processing, market trends and customer needs
and demands will be included. Decisions based on this variety of information will be
facilitated by dashboards and multi-criteria-optimisation (MCO) tools. These tools
are particularly useful to identify best compromises when dealing with conflicting
objectives, which  are typical in materials design (e.g. lighter-stiffer, cheap-high
purity, etc.).


Computational tools
-------------------

Continuum modelling tools (openFoam), atomistic modelling
tools (Gromacs), simulation platform (Simphony with the FORCE BDSS WORKFLOW Manager),
MCO tools (Dakota,…), data-driven modelling tools (IBM Watson).

Experimental data
-----------------
used for input parameters, verification, validation activities
is made available by the end-user in the various databased plugged in including
GRANTA MI materials information management system and other DB backends that can
be integrated either via the SimPhoNy Open Simulation Platform or directly with
the ENTHOUGHT BDSS FORCE Workflow Manager.

Data/Information management
---------------------------

Both virtual and experimental data is handled by
the BDSS platform through plugins to various database and data space systems. For
example the GRANTA MI materials information management system and SimPhoNy DB
wrappers (supporting SQL, no SQL backend solutions), IBM DB solutions, or those
integrated with the modFRONTIER. All data generated in FORCE is casted in an
ontology based (EMMO compliant) common universal data structures that are
maintained (curated)
in various backend data repositories connected with the FORCE system. The users
of the FORCE platform will decide how much of this information can be shared
with third parties, if at all, and under which conditions. Further data management
will be provided by integration with the MARKETPLACE platform.

vi) Traceability: of decisions and data sources is supported by GRANTA MI
and output of BDSS workflow manager. The BDSS architectural diagram for
interoperability is illustrated in Figure 10. Traceability is facilitated by
the use of the ontology-based data structures and the various semantic aware
data repository and data management backends. The description of a workflow,
including the history of the entire sample and workflow is included.

vii) Quality assurance:  in FORCE the semantic aware ontology based data
structures include verification and validation attributes and allow various
quality assurance algorithms to be developed. In the current project, the
system will be able to provide at least measures for the validation of a model,
especially with respect to 1. Previous work, and 2. Provide guidance for
additional verification. QA in FORCE is hence an iterative process.
