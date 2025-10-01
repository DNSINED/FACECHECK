from __future__ import annotations
import argparse
import yaml
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="configs/train.yaml")
    args = parser.parse_args()
    cfg = yaml.safe_load(Path(args.config).read_text())
    print("[FakeCheck][eval] Loaded config.")
    print("AUROC=0.50 AUPRC=0.50 EER=0.50 (stub)")


if __name__ == "__main__":
    main()
