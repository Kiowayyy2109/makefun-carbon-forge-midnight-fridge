#!/usr/bin/env python3
"""Midnight Fridge Roast — roasting the fridge at 2am."""
import os

LINE = "It's 2am. The fridge light is on, the fridge is judging me, and frankly, it's right."
assert len(LINE) == 84, "entry must be exactly 84 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
