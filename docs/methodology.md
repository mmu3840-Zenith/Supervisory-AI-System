# Research Methodology

## Research Question

Can a centralized supervisory controller improve multi-agent
task allocation by detecting elevated failure risk and
redistributing workload?

## Experimental Factors

Independent factors:

- number of agents
- number of tasks
- task priority
- initial energy
- workload
- supervisory control enabled/disabled

## Primary Metrics

- task completion rate
- mean predicted failure risk
- number of failed agents
- number of task reallocations
- remaining energy
- makespan

## Baselines

The system is compared against a greedy nearest-agent strategy.

The supervisory configuration uses the same computational
environment while adding centralized risk assessment and
workload redistribution.

## Reproducibility

Experiments use fixed random seeds:

42, 7, 21, 99, 123

Repeated trials should be reported using mean and standard
deviation rather than a single favorable run.

## Scope

This repository evaluates a computational abstraction.
Results should not be interpreted as evidence of physical
robotic deployment, real-world safety, or clinical efficacy.
