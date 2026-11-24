#!/usr/bin/env python3
"""Write one funny single-line excuse a developer gives when code breaks
in production, to /output/entry.txt (at most 200 characters)."""

import os

LINE = (
    "Production broke because the .env file on the server still says "
    "localhost, and localhost is doing great, thanks for asking."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
