pliers.models
=============

.. contents:: Contents
    :local:

Base Model
----------

The base model defines a lot of common methods that are identical for all models - logging, saving, etc.

.. autoclass:: pliers.models.base_model.BaseModel
   :members:
   :undoc-members:
   :exclude-members: training
   :show-inheritance:


PLI models
--------------------

Protein–ligand interaction prediction models.
Calculate embeddings for ligands and proteins, then use an MLP to predict the final result.

.. currentmodule:: pliers.models.pli
.. autosummary::
   :nosignatures:
   :recursive:


.. automodule:: pliers.models.pli
   :members:
   :undoc-members:
   :exclude-members: training, shared_step
   :show-inheritance:


Baseline models
----------------

These models predict the baseline values for datasets.
They have no access to the features and operate solely on the labels of ligands and proteins,
so they measure how much of a benchmark is solvable from label frequencies alone.
The pipeline runs them on every split it builds and writes
``results/baseline/<split name>.json``.

.. currentmodule:: pliers.models.pli.baseline
.. autosummary::
   :nosignatures:
   :recursive:


.. automodule:: pliers.models.pli.baseline
   :members:
   :undoc-members:
   :show-inheritance:


Metrics
----------------

The two metrics the affinity literature reports that torchmetrics does not provide,
plus the skill score that makes any of them interpretable against a baseline.

.. currentmodule:: pliers.models.metrics
.. autosummary::
   :nosignatures:
   :recursive:


.. automodule:: pliers.models.metrics
   :members:
   :undoc-members:
   :exclude-members: training
   :show-inheritance:
