import pandas as pd
import numpy as np
from scipy.stats import laplace, t


chat_id = 461694118 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n=len(x)
    x_bar = sum(x) / n
    s = np.sqrt(sum([(xi - x_bar) ** 2 for xi in x]) / (n - 1))
    b = s / np.sqrt(2)
    lower_bound = x_bar - laplace.ppf(1 - p / 2, scale=b) * np.sqrt(2) / n
    upper_bound = x_bar + laplace.ppf(1 - p / 2, scale=b) * np.sqrt(2) / n
    return lower_bound, \
           upper_bound
