from __future__ import annotations
import argparse
from pathlib import Path


def detect(path: str) -> int:
    p = Path(path)
    print(f"[FakeCheck][cli] Detected path: {p}")
    print("[FakeCheck][cli] Stub: always Inconclusive.")
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(prog="fakecheck")
    sub = parser.add_subparsers(dest="cmd")
    d = sub.add_parser("detect")
    d.add_argument("path", type=str)
    args = parser.parse_args()

    if args.cmd == "detect":
        raise SystemExit(detect(args.path))
    parser.print_help()


if __name__ == "__main__":
    main()
