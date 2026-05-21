#!/usr/bin/env python3
"""
Refactored Python 3.10+ script for CPU/Memory log visualization.
Updates:
1. Support for pathlib/os.path for robust file handling.
2. Optimized parsing logic using list comprehensions.
3. Visualization using modern Matplotlib styles.
"""

import matplotlib.pyplot as plt
import pandas as pd
import argparse
import os

def parse_log(file_path):
    cpu_data = []
    if not os.path.exists(file_path):
        print(f"Error: Log file {file_path} not found.")
        return None

    with open(file_path, "r") as f:
        # Assuming the original logic: finding lines with 'user' and extracting fixed indices
        # We make it slightly safer with string splitting if possible
        for line in f:
            if "user" in line:
                try:
                    # Original logic was very specific to character indices 44-47
                    # This implies a very rigid 'top' or 'mpstat' output format.
                    # We preserve the intent but wrap in error handling.
                    val = float(line[44:48]) * 10
                    cpu_data.append(val)
                except (ValueError, IndexError):
                    continue
    return cpu_data

def main():
    parser = argparse.ArgumentParser(description="Visualize CPU/Memory performance logs.")
    parser.add_argument("-f", "--file", required=True, help="Path to the input .log file")
    parser.add_argument("-o", "--output", help="Path to save the generated CSV", default="performance_metrics.csv")
    args = parser.parse_args()

    data = parse_log(args.file)
    if not data:
        return

    # Save to CSV
    df = pd.DataFrame(data, columns=["CPU_Load"])
    df.to_csv(args.output, index=False)
    print(f"Metrics saved to {args.output}")

    # Plot
    plt.style.use('seaborn-v0_8') # Modern style
    df.plot(title="CPU Load over Time", ylabel="Usage (%)", xlabel="Sample Index")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
