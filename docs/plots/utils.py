import matplotlib.pyplot as plt
import numpy as np
import os

def get_output_path(filename):
    output_dir = os.path.join(os.path.dirname(__file__), '..', 'images')
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, filename)