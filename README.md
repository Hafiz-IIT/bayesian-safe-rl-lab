# Bayesian Safe RL Lab

> **Research prototype:** uncertainty-aware action gating using a simple Bayesian-style dynamics uncertainty model.

## Research question
How should uncertainty in the transition model affect an action-authorization decision?

## Implemented
- scalar uncertain dynamics representation
- uncertainty-aware predicted interval
- explicit safety threshold
- deterministic decision logic
- reproducible tests

## Quickstart
```bash
python demo.py
python -m unittest discover -s tests -v
```

## Boundary
This is a research prototype, not Bayesian certification, formal safety assurance, or deployment-ready RL.

Related: [Safe RL Action Gate](https://github.com/Hafiz-IIT/safe-rl-action-gate)
