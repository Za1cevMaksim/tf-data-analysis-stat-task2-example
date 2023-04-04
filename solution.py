import pandas as pd
import numpy as np
from scipy.stats import laplace, t


chat_id = 461694118 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n = len(x)
    x_bar = np.mean(x)
    s = np.std(x, ddof=1)
    delta = 0.5 - np.exp(1)
    t_star = norm.ppf((1 + p) / 2)
    q = np.sqrt(8) / (1 + np.sqrt(8) * x_bar)
    d_q = -8 * np.sqrt(8) * (x_bar ** 2 + x_bar - 1) / ((1 + np.sqrt(8) * x_bar) ** 2)
    v = (s ** 2) * (1 - 2 * delta / n) / n
    d_v = (2 * delta / n ** 2) * (n * s ** 2 - (s ** 2) * (2 * n - 3))
    sigma_q = np.sqrt((d_q ** 2) * v + (q ** 2) * d_v)
    ME = t_star * sigma_q
    lower_bound = abs(q - ME)
    upper_bound = q + ME


    return lower_bound, \
           upper_bound
