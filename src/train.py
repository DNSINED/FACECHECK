from __future__ import annotations
import argparse
import yaml
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=str, default="configs/train.yaml")
    args = parser.parse_args()

    cfg = yaml.safe_load(Path(args.config).read_text())
    print("[FakeCheck][train] Loaded config:")
    print(yaml.dump(cfg, sort_keys=False))
    print("[FakeCheck][train] Stub finished.")


if __name__ == "__main__":
    main()
