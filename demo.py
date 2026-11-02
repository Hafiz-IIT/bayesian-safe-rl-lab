"""Show posterior uncertainty shrinking as scalar observations arrive."""
from uncertainty_gate import GaussianPosterior, authorize

posterior = GaussianPosterior(mean=0.0, variance=1.0)
for observation in (0.72, 0.81, 0.77):
    posterior = posterior.update(observation, observation_variance=0.04)
    interval = posterior.credible_interval(z_score=1.96)
    print(f"posterior={posterior}; interval={interval}; gate={authorize(interval, 0.9)}")
