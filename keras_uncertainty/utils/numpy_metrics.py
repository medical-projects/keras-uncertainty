# Metrics useful for uncertainty quantification, implemented using numpy.

import numpy as np

def accuracy(y_true, y_pred):
    return np.mean(y_true == y_pred)

EPSILON = 1e-7

def numpy_negative_log_likelihood(y_true, y_pred):
    """
        Negative log-likelihood or negative log-probability loss/metric.
        Reference: Evaluating Predictive Uncertainty Challenge, Quiñonero-Candela et al, 2006.
        It sums over classes: log(y_pred) for true class and log(1.0 - pred) for not true class, and then takes average across samples.
    """
    y_pred = np.clip(y_pred, EPSILON, 1.0 - EPSILON)

    return -np.mean(np.sum(y_true * np.log(y_pred) + (1.0 - y_true) * np.log(1.0 - y_pred), axis=-1), axis=-1)

def entropy(y_true, y_pred):
    return 0