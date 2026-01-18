import os
import pandas as pd
import numpy as np


def topsis(input_file, weights, impacts, output_file):

    if not os.path.exists(input_file):
        raise FileNotFoundError(f"File not found: {input_file}")

    df = pd.read_csv(input_file)

    if df.shape[1] < 3:
        raise ValueError("Input file must contain three or more columns.")

    data = df.iloc[:, 1:].copy()

    weights_list = weights.split(",")
    impacts_list = impacts.split(",")

    if len(weights_list) != data.shape[1]:
        raise ValueError("Number of weights must be equal to number of criteria columns.")

    if len(impacts_list) != data.shape[1]:
        raise ValueError("Number of impacts must be equal to number of criteria columns.")

    for imp in impacts_list:
        if imp not in ["+", "-"]:
            raise ValueError("Impacts must be either '+' or '-'.")

    try:
        weights_arr = np.array([float(x) for x in weights_list])
    except:
        raise ValueError("Weights must be numeric and separated by commas.")

    for col in data.columns:
        if not pd.api.types.is_numeric_dtype(data[col]):
            raise ValueError(f"Column '{col}' contains non-numeric values.")

    norm = np.sqrt((data ** 2).sum())
    normalized_data = data / norm

    weighted_data = normalized_data * weights_arr

    ideal_best = []
    ideal_worst = []

    for j in range(weighted_data.shape[1]):
        if impacts_list[j] == "+":
            ideal_best.append(weighted_data.iloc[:, j].max())
            ideal_worst.append(weighted_data.iloc[:, j].min())
        else:
            ideal_best.append(weighted_data.iloc[:, j].min())
            ideal_worst.append(weighted_data.iloc[:, j].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    df["Topsis Score"] = score
    df["Rank"] = df["Topsis Score"].rank(ascending=False).astype(int)

    df.to_csv(output_file, index=False)

    return output_file
