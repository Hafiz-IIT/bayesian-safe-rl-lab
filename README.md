# Bayesian Safe RL Lab

A compact decision-gating prototype that updates a scalar Gaussian belief from observations and uses an uncertainty interval to choose between ALLOW, VERIFY, and BLOCK.

## Research question
How should uncertainty in a predicted hazard influence whether an autonomous controller proceeds, gathers more evidence, or defers an action?

## Implemented
- Normal-Normal conjugate posterior update with known observation variance
- uncertainty interval construction using a configurable z-score
- conservative three-way action gate
- finite-value and variance validation
- deterministic demo and unit tests

## Decision rule
For predicted interval [mu-r, mu+r] and threshold tau:
- ALLOW if the entire interval is at or below tau
- VERIFY if the interval overlaps tau
- BLOCK if the entire interval is above tau

This is an illustrative scalar rule. It is not automatically calibrated and is not a formal safety guarantee.

## Run
    python demo.py
    python -m unittest discover -s tests -v

## Limitations
The model is scalar, assumes known observation noise, and does not represent sequential control dynamics or policy learning. It is not a complete Bayesian reinforcement-learning algorithm.

See [EVALUATION.md](EVALUATION.md) for the proposed calibration and stress-test protocol.
