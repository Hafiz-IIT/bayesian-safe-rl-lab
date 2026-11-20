"""Conjugate Gaussian uncertainty gate for a scalar predicted hazard.

This is a toy scalar posterior and conservative threshold rule, not a complete
Bayesian RL algorithm, calibrated risk model, or safety proof.
"""
from dataclasses import dataclass
import math

def _finite(name: str, value: float) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a finite number")
    try:
        normalized = float(value)
    except (OverflowError, TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be a finite number") from exc
    if not math.isfinite(normalized):
        raise ValueError(f"{name} must be a finite number")
    return normalized

@dataclass(frozen=True)
class DynamicsEstimate:
    mean: float
    radius: float
    def __post_init__(self):
        _finite("mean", self.mean)
        radius = _finite("radius", self.radius)
        if radius < 0: raise ValueError("radius must be non-negative")

@dataclass(frozen=True)
class GaussianPosterior:
    mean: float = 0.0
    variance: float = 1.0
    def __post_init__(self):
        _finite("mean", self.mean)
        variance = _finite("variance", self.variance)
        if variance <= 0: raise ValueError("posterior variance must be positive")

    def update(self, observation: float, observation_variance: float) -> "GaussianPosterior":
        """Normal-Normal update with known observation variance, using stable weights."""
        observation = _finite("observation", observation)
        observation_variance = _finite("observation_variance", observation_variance)
        if observation_variance <= 0: raise ValueError("observation_variance must be positive")
        prior_variance = self.variance
        if prior_variance >= observation_variance:
            ratio = observation_variance / prior_variance
            prior_weight = ratio / (1.0 + ratio)
            observation_weight = 1.0 / (1.0 + ratio)
            variance = observation_variance / (1.0 + ratio)
        else:
            ratio = prior_variance / observation_variance
            prior_weight = 1.0 / (1.0 + ratio)
            observation_weight = ratio / (1.0 + ratio)
            variance = prior_variance / (1.0 + ratio)
        mean = prior_weight * self.mean + observation_weight * observation
        if not math.isfinite(mean) or not math.isfinite(variance) or variance <= 0:
            raise OverflowError("posterior update is outside representable numeric range")
        return GaussianPosterior(mean, variance)

    def credible_interval(self, z_score: float = 1.96) -> DynamicsEstimate:
        z_score = _finite("z_score", z_score)
        if z_score < 0: raise ValueError("z_score must be non-negative")
        return DynamicsEstimate(self.mean, z_score * math.sqrt(self.variance))

def authorize(predicted: DynamicsEstimate, limit: float) -> str:
    """ALLOW only if the entire interval is below the limit; otherwise VERIFY/BLOCK."""
    if not isinstance(predicted, DynamicsEstimate):
        raise TypeError("predicted must be a DynamicsEstimate")
    limit = _finite("limit", limit)
    upper = predicted.mean + predicted.radius
    lower = predicted.mean - predicted.radius
    if not math.isfinite(upper) or not math.isfinite(lower):
        return "VERIFY"
    if upper <= limit: return "ALLOW"
    if lower <= limit: return "VERIFY"
    return "BLOCK"
