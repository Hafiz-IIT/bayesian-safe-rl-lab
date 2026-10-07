from dataclasses import dataclass

@dataclass(frozen=True)
class DynamicsEstimate:
    mean: float
    radius: float

def authorize(predicted: DynamicsEstimate, limit: float) -> str:
    upper = predicted.mean + predicted.radius
    lower = predicted.mean - predicted.radius
    if upper <= limit:
        return "ALLOW"
    if lower <= limit:
        return "VERIFY"
    return "BLOCK"
