#!/usr/bin/env python3
"""Summarize WRO distance-sensor CSV logs without discarding invalid rows."""

from __future__ import annotations

import argparse
import csv
import math
import statistics
from collections import defaultdict
from pathlib import Path


GROUP_FIELDS = ("sensor", "true_distance_cm", "surface", "mode")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Calculate mean, median, MAE, population standard deviation, and invalid counts."
    )
    parser.add_argument("csv_file", type=Path, help="CSV file using the validation-protocol schema")
    return parser.parse_args()


def is_valid(row: dict[str, str]) -> bool:
    marker = row.get("valid", "").strip().lower()
    if marker in {"0", "false", "no", "invalid"}:
        return False
    try:
        return math.isfinite(float(row.get("reading_cm", "")))
    except (TypeError, ValueError):
        return False


def format_number(value: float | None) -> str:
    return "—" if value is None else f"{value:.3f}"


def main() -> None:
    args = parse_args()
    groups: dict[tuple[str, ...], list[dict[str, str]]] = defaultdict(list)

    with args.csv_file.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = set(GROUP_FIELDS + ("reading_cm", "valid")) - set(reader.fieldnames or [])
        if missing:
            raise SystemExit(f"Missing required columns: {', '.join(sorted(missing))}")
        for row in reader:
            groups[tuple(row.get(field, "").strip() for field in GROUP_FIELDS)].append(row)

    header = (
        "sensor", "true_cm", "surface", "mode", "valid", "invalid",
        "invalid_%", "mean_cm", "median_cm", "mae_cm", "stddev_cm",
    )
    print("\t".join(header))

    for key in sorted(groups):
        rows = groups[key]
        valid_rows = [row for row in rows if is_valid(row)]
        values = [float(row["reading_cm"]) for row in valid_rows]
        invalid_count = len(rows) - len(values)

        try:
            true_distance = float(key[1])
        except ValueError:
            true_distance = None

        mean = statistics.fmean(values) if values else None
        median = statistics.median(values) if values else None
        mae = (
            statistics.fmean(abs(value - true_distance) for value in values)
            if values and true_distance is not None
            else None
        )
        stddev = statistics.pstdev(values) if values else None
        invalid_percent = 100 * invalid_count / len(rows) if rows else 0.0

        output = (
            key[0], key[1], key[2], key[3], str(len(values)), str(invalid_count),
            f"{invalid_percent:.1f}", format_number(mean), format_number(median),
            format_number(mae), format_number(stddev),
        )
        print("\t".join(output))


if __name__ == "__main__":
    main()
