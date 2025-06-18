import numpy as np
from scipy import stats


def stability_index(metric_vector, falling_rate_weight=12, variability_weight=0.5):
    """Calculates a stability metric for a given sequence of metric values.

    The stability metric is computed as the mean of the metric vector, penalized by the rate of decrease (slope)
    and the variability (standard deviation of residuals) in the sequence. A negative slope (falling rate) incurs
    a penalty weighted by `falling_rate_weight`, and higher variability incurs a penalty weighted by `variability_weight`.

    Args:
        metric_vector (array-like): Sequence of metric values to evaluate stability.
        falling_rate_weight (float, optional): Weight for penalizing negative slope (default is 12).
        variability_weight (float, optional): Weight for penalizing variability (default is 0.5).
        
    Returns:
        float: The computed stability metric, where higher values indicate greater stability.
    """
    metric_vector = np.array(metric_vector)
    t = np.arange(len(metric_vector))

    slope, intercept, _, _, _ = stats.linregress(t, metric_vector)
    
    predicted = intercept + slope * t
    residuals = metric_vector - predicted
    mean_metric = np.mean(metric_vector)

    falling_rate_penalty = falling_rate_weight * min(0, slope)
    variability_penalty = variability_weight * np.std(residuals)

    stability_metric = mean_metric + falling_rate_penalty - variability_penalty

    return stability_metric