"""Conjugate Gaussian uncertainty gate for a scalar predicted hazard.

The module demonstrates posterior updating and conservative action gating.
It is a toy decision model, not a complete Bayesian RL algorithm or safety proof.
"""
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class DynamicsEstimate:
    mean: float
    radius: float

    def __post_init__(self):
        if not math.isfinite(self.mean) or not math.isfinite(self.radius) or self.radius < 0:
            raise ValueError("mean must be finite and radius finite/non-negative")


@dataclass(frozen=True)
class GaussianPosterior:
    mean: float = 0.0
    variance: float = 1.0

    def __post_init__(self):
        if not math.isfinite(self.mean) or not math.isfinite(self.variance) or self.variance <= 0:
            raise ValueError("posterior variance must be finite and positive")

    def update(self, observation: float, observation_variance: float) -> "GaussianPosterior":
        """Normal-Normal update with a known observation variance."""
        if not math.isfinite(observation) or not math.isfinite(observation_variance) or observation_variance <= 0:
            raise ValueError("observation and positive variance must be finite")
        prior_precision = 1.0 / self.variance
        observation_precision = 1.0 / observation_variance
        variance = 1.0 / (prior_precision + observation_precision)
        mean = variance * (self.mean * prior_precision + observation * observation_precision)
        return GaussianPosterior(mean, variance)

    def credible_interval(self, z_score: float = 1.96) -> DynamicsEstimate:
        if not math.isfinite(z_score) or z_score < 0:
            raise ValueError("z_score must be finite and non-negative")
        return DynamicsEstimate(self.mean, z_score * math.sqrt(self.variance))


def authorize(predicted: DynamicsEstimate, limit: float) -> str:
    """ALLOW only if the entire interval is below the limit; otherwise VERIFY/BLOCK."""
    if not math.isfinite(limit):
        raise ValueError("limit must be finite")
    upper = predicted.mean + predicted.radius
    lower = predicted.mean - predicted.radius
    if upper <= limit:
        return "ALLOW"
    if lower <= limit:
        return "VERIFY"
    return "BLOCK"
