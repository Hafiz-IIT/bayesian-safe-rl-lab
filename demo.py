from uncertainty_gate import DynamicsEstimate, authorize

for estimate in [DynamicsEstimate(0.5,0.1), DynamicsEstimate(0.8,0.2), DynamicsEstimate(1.2,0.1)]:
    print(estimate, "->", authorize(estimate, 0.9))
