import math

from typing import List, Sized

import numpy


def weighted_statistics(values: Sized, weights: Sized) -> List[float]:
    """Return the weighted average, standard deviation, N and standard error."""
    average = numpy.average(values, weights=weights, axis=0)[0]
    # Fast and numerically precise:
    variance = numpy.average((values - average) ** 2, weights=weights, axis=0)
    sd = math.sqrt(variance)
    error = 1.96 * sd / math.sqrt(len(values))
    return [average, math.sqrt(variance), len(values), error]
