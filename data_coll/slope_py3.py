#!/usr/bin/env python3
"""
Refactored Python 3.10+ script for calculating slope of CPU usage.
Updates:
1. Support for dynamic file paths.
2. Robust indexing with error handling.
"""

import pandas as pd
import numpy as np
import argparse
import os

def main():
    parser = argparse.ArgumentParser(description="Calculate CPU usage slope.")
    parser.add_argument("-f", "--file", required=True, help="Path to the input .csv file")
    parser.add_argument("-s", "--start", type=int, default=100, help="Start index for slope calculation")
    parser.add_argument("-e", "--end", type=int, default=150, help="End index for slope calculation")
    args = parser.parse_args()

    if not os.path.exists(args.file):
        print(f"Error: File {args.file} not found.")
        return

    try:
        cpu_data = pd.read_csv(args.file, header=None)
        cpu_load = cpu_data[0]
        
        if args.end >= len(cpu_load) or args.start < 0:
            print(f"Error: Indices {args.start}-{args.end} are out of bounds for data length {len(cpu_load)}.")
            return

        slope = (cpu_load[args.end] - cpu_load[args.start]) / (args.end - args.start)
        print(f"Slope for data (indices {args.start} to {args.end}): {slope:.4f}")
        
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    main()
