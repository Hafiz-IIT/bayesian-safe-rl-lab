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

    def test_extreme_variances_do_not_overflow_precision(self):
        prior = GaussianPosterior(1.0, 1e300)
        posterior = prior.update(2.0, 1e300)
        self.assertAlmostEqual(posterior.mean, 1.5)
        self.assertTrue(posterior.variance > 0)

    def test_nonfinite_observation_rejected(self):
        with self.assertRaises(ValueError):
            GaussianPosterior().update(float("nan"), 1.0)

    def test_extremely_large_integer_inputs_are_rejected_cleanly(self):
        huge = 10 ** 10000
        with self.assertRaises(ValueError):
            GaussianPosterior(huge, 1.0)
        with self.assertRaises(ValueError):
            GaussianPosterior().update(1.0, huge)
        with self.assertRaises(ValueError):
            GaussianPosterior().credible_interval(huge)

    def test_invalid_variance(self):
        with self.assertRaises(ValueError):
            GaussianPosterior(0.0, 0.0)

if __name__ == "__main__": unittest.main()
