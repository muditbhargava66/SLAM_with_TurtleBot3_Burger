#!/usr/bin/env python3
"""
Refactored Python 3.10+ script for similarity metrics.
Updates: 
1. Use skimage.metrics.structural_similarity (the new API).
2. Dynamic directory handling.
3. SSIM Multichannel fix.
"""

import numpy as np
import argparse
import cv2
import os
from skimage.metrics import structural_similarity as ssim

def similarity_score(imageA, imageB, name):
    def mse(imageA, imageB):
        error = np.sum((imageA.astype("float") - imageB.astype("float"))**2)
        error /= float(imageA.shape[0] * imageA.shape[1])
        return error

    m = mse(imageA, imageB)
    # multichannel=True is deprecated in favor of channel_axis
    s = ssim(imageA, imageB, channel_axis=2)

    print(f"{name} MSE: {m:.2f}, SSIM: {s:.2f}")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--dir", required=True, help="path to directory containing maps")
    args = vars(ap.parse_args())

    target_dir = args["dir"]
    if not os.path.exists(target_dir):
        print(f"Error: Directory {target_dir} not found.")
        return

    map_list = sorted([f for f in os.listdir(target_dir) if f.endswith(('.png', '.pgm', '.jpg'))])
    
    if len(map_list) < 2:
        print("Error: Need at least 2 map images to compare.")
        return

    print(f"Found maps: {map_list}")

    # Load and resize to a consistent size for comparison
    # Original used (197, 578) - preserving that logic but making it robust
    standard_size = (197, 578)
    
    images = {}
    for map_file in map_list:
        img_path = os.path.join(target_dir, map_file)
        img = cv2.imread(img_path)
        if img is not None:
            images[map_file] = cv2.resize(img, dsize=standard_size, interpolation=cv2.INTER_CUBIC)
        else:
            print(f"Warning: Could not read {map_file}")

    # Example comparisons (Dynamic based on availability)
    processed_maps = list(images.keys())
    for i in range(len(processed_maps)):
        for j in range(i + 1, len(processed_maps)):
            name_a = processed_maps[i]
            name_b = processed_maps[j]
            similarity_score(images[name_a], images[name_b], f"Comparing {name_a} vs {name_b} : ")

if __name__ == "__main__":
    main()
