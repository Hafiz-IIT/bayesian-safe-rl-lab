import unittest
from uncertainty_gate import GaussianPosterior, authorize

class PosteriorTests(unittest.TestCase):
    def test_update_moves_toward_observation(self):
        prior = GaussianPosterior(0.0, 1.0)
        posterior = prior.update(2.0, 0.25)
        self.assertGreater(posterior.mean, prior.mean)
        self.assertLess(posterior.variance, prior.variance)

    def test_interval_gate_defers_when_uncertain(self):
        estimate = GaussianPosterior(0.8, 0.1).credible_interval()
        self.assertEqual(authorize(estimate, 0.9), "VERIFY")

    def test_invalid_variance(self):
        with self.assertRaises(ValueError):
            GaussianPosterior(0.0, 0.0)

if __name__ == "__main__": unittest.main()
