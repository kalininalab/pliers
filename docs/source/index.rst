Welcome to PLIERS's documentation!
====================================

:github_url: https://github.com/kalininalab/pliers

PLIERS Documentation
=====================

Welcome to PLIERS's documentation!
This is a collection of various models and utilities that are focused on using residue-level
protein contact graphs - one node per residue, edges between residues whose C-alpha atoms lie
within a distance cutoff - for predicting protein–ligand interactions.



.. toctree::
   :glob:
   :maxdepth: 1
   :caption: Notes

   notes/installation
   notes/quick_start
   notes/snakemake
   notes/data
   notes/training


.. toctree::
   :glob:
   :maxdepth: 1
   :caption: Package Reference

   modules/models
   modules/layers
   modules/data
   modules/utils

.. autosummary::
   :toctree: _autosummary
   :recursive:

Indices and tables
===================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
