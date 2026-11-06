import numpy as np
import pandas as pd

from .base_baseline import BaseBaseline


class ProteinLigandMax(BaseBaseline):
    """Take the average of the ligand and protein labels."""

    def __init__(self, which: str = "both", prob: bool = False, task: str = "class"):
        super().__init__(prob, task)
        self.which = which

    def fit(self, train: pd.DataFrame):
        """Fit the model to the training dataframe. Has to have 'Drug_ID', 'Target_ID' and 'Y' columns.

        The column names are the pipeline's on-disk table format and predate the rename
        to protein/ligand wording; they are deliberately unchanged, since every published
        dataset hash is computed from them.
        """
        train["count"] = 1
        self.protgroup = train.groupby("Target_ID").agg({"Y": ["mean", "std"], "count": "sum"}).loc[:, "Y"]
        self.druggroup = train.groupby("Drug_ID").agg({"Y": ["mean", "std"], "count": "sum"}).loc[:, "Y"]
        # An unseen protein or ligand gets an uninformative prior: a coin flip for a binary
        # label, the train mean for an affinity (0.5 would be a pKd of 0.5).
        self.fallback = train["Y"].mean() if self.task == "reg" else 0.5

    def _get_val(self, group: pd.DataFrame, id: str) -> float:
        if id not in group.index:
            return self.fallback
        elif self.prob:
            return np.random.normal(loc=group.at[id, "mean"], scale=group.at[id, "std"])
        return group.at[id, "mean"]

    def predict_pair(self, prot_id: str, drug_id: str) -> float:
        """Predict the outcome for a pair of a protein and a ligand."""
        if self.which == "both":
            return (self._get_val(self.protgroup, prot_id) + self._get_val(self.druggroup, drug_id)) / 2
        elif self.which == "protein":
            return self._get_val(self.protgroup, prot_id)
        elif self.which == "ligand":
            return self._get_val(self.druggroup, drug_id)
        else:
            raise ValueError(f"Unknown value for which: {self.which}")
