import pandas as pd
import numpy as np
from scipy.stats import laplace, t


chat_id = 461694118 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n=len(x)
    x_bar = np.mean(x)
    SE_x_bar = np.std(x, ddof=1) / np.sqrt(n)
    time = 8
    a_hat = 2 * x_bar / time ** 2

    SE_a_hat = 2 * SE_x_bar / time ** 2
    alpha = 1-p  # significance level
    df = n - 1  # degrees of freedom
    t_crit = t.ppf(1 - alpha / 2, df)
    CI = a_hat + np.array([-1, 1]) * t_crit * SE_a_hat



    return CI[0], \
           CI[1]
