import pandas as pd
import numpy as np
from scipy.stats import t


chat_id = 461694118 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    x_bar = sum(x) / n
    s = np.sqrt(sum([(xi - x_bar) ** 2 for xi in x]) / (n - 1))
    df = n - 1
    t_value = t.ppf((1 + p) / 2, df)
    margin_error = t_value * s / np.sqrt(n)
    lower_bound = x_bar - margin_error
    upper_bound = x_bar + margin_error
    return lower_bound, \
           upper_bound
