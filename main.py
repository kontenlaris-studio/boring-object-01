#!/usr/bin/env python3
"""The Most Boring Object, Reviewed in One Line.

One-line review of the most boring everyday object I could name:
the humble light switch. Five stars, deadpan, true: two settings,
zero updates in 40 years, and it still beats every smart device
in the house. The review format is the joke's delivery: a five-star
verdict for an object that has never once asked to be reviewed.
"""

import os

LINE = (
    "★★★★★ for the light switch: two settings, zero updates in 40 years, "
    "and it still outperforms every smart device in this house."
)


def main() -> None:
    print(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
