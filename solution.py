import pandas as pd
import numpy as np
from scipy.stats import t


chat_id = 461694118 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    n=len(x)
    x_bar = np.mean(x)
    SE_x_bar = np.std(x, ddof=1) / np.sqrt(n)
    time = 8
    a_hat = 2 * x_bar / time ** 2

    SE_a_hat = 2 * SE_x_bar / time ** 2
    alpha = 1-p
    df = n - 1
    t_crit = t.ppf(1 - alpha / 2, df)
    er=t_crit * SE_a_hat
    upper_bound = a_hat + er
    lower_bound=a_hat-er

    return lower_bound, \
           upper_bound
