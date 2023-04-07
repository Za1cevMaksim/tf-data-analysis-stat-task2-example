import pandas as pd
import numpy as np
from scipy.stats import t


chat_id = 461694118 

def solution(p: float, x: np.array) -> tuple:
    n=len(x)
    t = 8
    d1=(-np.log(p))/n
    d2 = (-np.log(1-p))/n
    lower_bound=2*(d1-1/2+min(x))/t**2
    upper_bound=2*(d2-1/2+min(x))/t**2
    return lower_bound, \
           upper_bound
