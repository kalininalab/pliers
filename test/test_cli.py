"""Tests for the training entry point's guards."""

import pytest

from pliers.cli import check_dataset_file, check_task_matches


class _FakeDataModule:
    def __init__(self, task):
        config = {"snakemake": {}}
        if task is not None:
            config["snakemake"]["parse_dataset"] = {"task": task}
        self.config = config


class TestCheckTaskMatches:
    """`parse_dataset.task` and `model.module` live in separate config files.

    Nothing related them, so a `reg` dataset trained as `class` ran
    binary_cross_entropy_with_logits against continuous affinities and reported AUROC on
    them without error.
    """

    @pytest.mark.parametrize("task", ["class", "reg"])
    def test_matching_task_passes(self, task):
        check_task_matches(_FakeDataModule(task), task)

    @pytest.mark.parametrize(("task", "module"), [("reg", "class"), ("class", "reg")])
    def test_mismatch_raises(self, task, module):
        with pytest.raises(ValueError, match="parse_dataset.task"):
            check_task_matches(_FakeDataModule(task), module)

    def test_dataset_without_recorded_task_is_allowed(self):
        """Datasets built before the task was recorded must still load."""
        check_task_matches(_FakeDataModule(None), "class")


class TestCheckDatasetFile:
    """Every shipped config leaves `datamodule.filename` null; say so instead of a TypeError."""

    @pytest.mark.parametrize("config", [{"datamodule": {"filename": None}}, {"datamodule": {}}, {}])
    def test_unset_filename_names_the_key(self, config):
        with pytest.raises(ValueError, match="datamodule.filename is not set"):
            check_dataset_file(config)

    def test_missing_file_names_the_path(self, tmp_path):
        with pytest.raises(FileNotFoundError, match="nope.pkl"):
            check_dataset_file({"datamodule": {"filename": str(tmp_path / "nope.pkl")}})

    def test_existing_file_passes(self, tmp_path):
        path = tmp_path / "data.pkl"
        path.write_bytes(b"")
        check_dataset_file({"datamodule": {"filename": str(path)}})
