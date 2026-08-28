"""Research plotting utilities.

Plots consume recorded experimental data only.
No experimental result is hard-coded.
"""

from __future__ import annotations

from pathlib import Path
from typing import Sequence

import matplotlib.pyplot as plt


def plot_comparison(
    labels: Sequence[str],
    values: Sequence[float],
    ylabel: str,
    title: str,
    output_path: str | Path,
) -> Path:
    """Create a simple comparison figure."""

    if len(labels) != len(values):
        raise ValueError(
            "labels and values must have equal length"
        )

    if not labels:
        raise ValueError(
            "at least one value is required"
        )

    output = Path(output_path)
    output.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    figure = plt.figure()
    axis = figure.add_subplot(111)

    axis.bar(labels, values)
    axis.set_title(title)
    axis.set_ylabel(ylabel)
    axis.grid(
        True,
        axis="y",
        alpha=0.3,
    )

    figure.tight_layout()
    figure.savefig(
        output,
        dpi=300,
    )
    plt.close(figure)

    return output
