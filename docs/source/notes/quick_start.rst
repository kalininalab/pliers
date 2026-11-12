Quick start guide
=================

This assumes you have followed :doc:`installation` and the environment is active
(``source .venv/bin/activate``). Run every command from the repository root.

The bundled example
-------------------

The repository ships a small test dataset (five proteins, five ligands), so the whole
path from structures to a trained model takes about a minute, with or without a GPU.

.. code:: console

    # 1. Build the graph dataset (about 30 s)
    snakemake -s workflow/Snakefile -j4 --configfile config/snakemake/test.yaml

    # 2. Train one short run (a few seconds on a CPU)
    pliers-train config/pli/quickstart.yaml

    # 3. Inspect
    tensorboard --logdir=tb_logs

Step 1 writes ``test/test_data/results/prepare_all/nlpncnndlwr_5f8b1046.pkl``. The name
is derived from the snakemake config, which is why ``config/pli/quickstart.yaml`` can
point at it directly. Step 2 ends by printing test metrics. With only three test
interactions they show that everything works, not how good the model is.

To turn the logs into a table:

.. code:: console

    python -m pliers.utils.results --logdir tb_logs --output results.csv --summary true

A real dataset: GLASS
---------------------

The same three steps on the `GLASS dataset <https://zhanggroup.org/GLASS/>`_, a set
of GPCR-ligand interactions.

**Download.** ``get_datasets.py`` needs PyTDC, which pins ``numpy<2`` and so cannot share
an environment with the training stack. The script declares its own dependencies
(PEP 723), so run it with ``uv run``, not ``python``:

.. code:: console

    uv run workflow/scripts/get_datasets.py glass --min_num_aa 250 --download_structures true

``--min_num_aa 250`` drops structures shorter than 250 residues, which for GPCRs are
fragments. The data lands in ``datasets/glass/resources``, with AlphaFold models in
``structures/``.

**Build the dataset.**

.. code:: console

    snakemake -s workflow/Snakefile -j 10 --configfile config/snakemake/glass.yaml

The GLASS config uses a random split, so no conda environment is needed. Add
``--software-deployment-method conda`` only for ``split_data.method: cluster_target``,
which needs MMseqs2 (see :doc:`installation`).

**Find the file it built.** The output is named by a hash of the snakemake config, so
every shipped training config leaves ``datamodule.filename`` as ``null``. List what you
have built, and the config behind each file:

.. code:: console

    python workflow/scripts/dataset_index.py 'datasets/glass/results/prepare_all/*.pkl'

**Train.** Pass the path from the listing:

.. code:: console

    pliers-train config/pli/glass.yaml \
        --set datamodule.filename=datasets/glass/results/prepare_all/<hash>.pkl

Training on the full dataset takes a while. Follow it with
``tensorboard --logdir=tb_logs``.
