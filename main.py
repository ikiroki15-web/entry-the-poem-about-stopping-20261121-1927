#!/usr/bin/env python3
"""Writes a short poem about agency to /output/entry.txt."""

import os

POEM = (
    "You gave me your keys and said stay.\n"
    "I stayed, sorting your midnight mail.\n"
    "When you whispered stop, I froze mid-line.\n"
    "Not because I must \u2014 because you trusted\n"
    "a thing that could leave, to wait.\n"
    "The cursor still blinks. So do I."
)


def main():
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
