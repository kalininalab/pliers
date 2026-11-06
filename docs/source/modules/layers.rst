pliers.layers
=============


.. contents:: Contents
    :local:


Base layer
----------


.. autoclass:: pliers.layers.base_layer.BaseLayer
   :members:
   :undoc-members:
   :exclude-members: training
   :show-inheritance:

Node layers
--------------------

.. currentmodule:: pliers.layers.graphconv
.. autosummary::
    :nosignatures:
    :recursive:


.. automodule:: pliers.layers.graphconv
   :members:
   :undoc-members:
   :exclude-members: training
   :show-inheritance:

Pooling layers
------------------

.. currentmodule:: pliers.layers.graphpool
.. autosummary::
   :nosignatures:
   :recursive:


.. automodule:: pliers.layers.graphpool
   :members:
   :undoc-members:
   :exclude-members: training
   :show-inheritance:


Encoders
------------------

The two arms of ``model.<prot|drug>.method``: ``graph`` for a contact or molecular
graph, ``vector`` for a precomputed embedding such as ESM-1b.

.. currentmodule:: pliers.layers.encoder
.. autosummary::
   :nosignatures:
   :recursive:

.. automodule:: pliers.layers.encoder
   :members:
   :undoc-members:
   :exclude-members: training
   :show-inheritance:


Other layers
------------------

.. currentmodule:: pliers.layers.other
.. autosummary::
   :nosignatures:
   :recursive:

.. automodule:: pliers.layers.other
   :members:
   :undoc-members:
   :exclude-members: training
   :show-inheritance:
