import pandas as pd
import numpy as np
from scipy import stats


chat_id = 399364172

def solution(sample1: np.array, sample2: np.array) -> bool:
    ks_stat, p_value = stats.ks_2samp(sample1, sample2)
    
    return p_value > 0.07:
