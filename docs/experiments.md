# Experimental Design

Each experimental condition is executed using deterministic
random seeds.

For each seed:

1. Generate the same computational environment.
2. Initialize the same number of simulated agents.
3. Generate the same task distribution.
4. Run the baseline controller.
5. Run the supervisory controller.
6. Record the resulting metrics.
7. Aggregate repeated trials.

The comparison is designed to isolate the contribution of
supervisory failure-risk monitoring and workload redistribution.
