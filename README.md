# Bayesian Safe RL Lab

> **Research prototype:** uncertainty-aware action gating using a simple Bayesian-style dynamics uncertainty model.

## Research question

<p align="center"><a href="https://github.com/Hafiz-IIT/bayesian-safe-rl-lab/actions"><img src="https://img.shields.io/github/actions/workflow/status/Hafiz-IIT/bayesian-safe-rl-lab/ci.yml?label=CI" alt="CI"/></a></p>
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
\n\n## Example and evidence boundary\n\nRun `demo.py` for the reference decision path and `tests/` for deterministic behavior.\n\n## Results and limitations\n\nThe prototype demonstrates uncertainty-aware gating using a deliberately simple scalar dynamics model. It is not a formal Bayesian inference system, a safety certificate, or evidence of deployment robustness. The uncertainty representation is a research abstraction whose assumptions must be replaced before real-world use.\n\n## Companion manuscript\n\nSee [Bayesian Safe RL — Research Manuscript](https://github.com/Hafiz-IIT/bayesian-safe-rl-paper).\n