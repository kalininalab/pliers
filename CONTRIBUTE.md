# PLIERS contribution guide

## Setup

```bash
uv sync --extra dev --extra workflow
uv run pre-commit install
```

`pyproject.toml` holds all tooling configuration (ruff, pytest, snakefmt).

Snakemake files are formatted with `snakefmt`, which is *not* part of pre-commit
because it needs the external [`shfmt`](https://github.com/mvdan/sh) binary to
format shell directives. If you edit `workflow/Snakefile` or `workflow/rules/*.smk`,
install `shfmt` and run `uv run snakefmt workflow/` by hand.

## Before committing

`pre-commit` runs ruff (lint + format) automatically on every commit.
To run everything by hand:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest -m "not gpu and not snakemake"
```

## Tests

| Command | Scope |
|---|---|
| `pytest -m "not gpu and not snakemake"` | Fast unit tests, no external tools |
| `pytest -m "snakemake and not gpu"` | Full pipeline; builds a conda env for MMseqs2 on first run |
| `pytest -m "not gpu"` | Everything except GPU tests |

Tests marked `snakemake` execute the real workflow on `test/test_data`, so keep them
out of tight edit loops.

## Adding a dependency

Add it to the right group in `pyproject.toml`, then regenerate the lockfile with
`uv lock` and commit `uv.lock` alongside your change.

Note that `workflow/scripts/get_datasets.py` deliberately declares its dependencies
inline (PEP 723) rather than in `pyproject.toml`, because PyTDC pins `numpy<2` and
cannot share an environment with the training stack.

## Documentation

The docs are Sphinx sources in `docs/source/`. Build them the way CI does, with
warnings as errors:

```bash
uv pip install -e ".[docs]"
uv run sphinx-build -W --keep-going -b html docs/source docs/_build
```

Read the Docs builds <https://pliers-bio.readthedocs.io> from `.readthedocs.yaml` on
every push to `main`, and fails on any Sphinx warning, so a docs build that is
clean locally is clean there. The API pages (`docs/source/modules/`) are generated
from docstrings; a new public module needs an entry there to appear.
