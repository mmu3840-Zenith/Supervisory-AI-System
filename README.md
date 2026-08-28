
Supervisory AI System
Centralized Supervisory Control for Multi-Agent Robotic Systems

A computational research framework investigating whether a
central supervisory controller can improve multi-agent task
allocation by monitoring simulated failure risk and dynamically
redistributing workload.

Important: This repository is a computational simulation.
It does not demonstrate physical robotic deployment.

Research Hypothesis

A centralized supervisory layer that continuously estimates
agent failure risk and redistributes workload should reduce
system-level degradation compared with a purely greedy
task-allocation strategy.

Architecture
Environment
     |
     v
Robot Agents
     |
     v
Failure-Risk Estimator
     |
     v
Supervisory Controller
     |
     +--------> Continue
     |
     +--------> Redistribute
                    |
                    v
              Task Allocation
                    |
                    v
              System Metrics
Core Components
Agent Layer

Each simulated robot maintains:

position
energy
workload
active/inactive state
completed-task count
Failure Prediction

A transparent energy/workload heuristic estimates failure
risk on a normalized [0, 1] scale.

Supervisory Controller

The supervisor:

observes agent state
estimates failure risk
identifies elevated-risk agents
triggers workload redistribution
Allocation

Two allocation strategies are available:

nearest-agent greedy allocation
workload-aware allocation

This allows the supervisory contribution to be evaluated
against a computational baseline.

Experimental Metrics

The experiment records:

MetricDescription
Completion RateFraction of tasks completed
Mean Failure RiskAverage predicted agent risk
Failed AgentsAgents that become inactive
Task ReassignmentsSupervisory workload redistribution events
Total EnergyRemaining swarm energy
MakespanNumber of simulation steps
Reproducibility

Experiments use fixed seeds:

42
7
21
99
123

This permits repeated evaluation under identical computational
conditions.

Running

Install dependencies:

pip install -r requirements.txt

Run tests:

python -m pytest -q

Run experiments:

python experiments/run_experiments.py

Aggregate results:

python -m src.experiments.aggregate

Raw results are written to:

results/raw/

Aggregated results are written to:

results/processed/
Research Integrity

The repository deliberately distinguishes between:

Demonstrated

computational multi-agent coordination
deterministic experiments
simulated failure-risk prediction
workload redistribution
quantitative evaluation

Not demonstrated

physical robotic deployment
real-world failure prediction
medical efficacy
biological performance
hardware validation

The objective is to provide a reproducible computational
framework that can later support more sophisticated models and
hardware experiments.

Project Structure
Supervisory-AI-System/
│
├── src/
│   ├── agents/
│   ├── environment/
│   ├── supervisor/
│   ├── prediction/
│   ├── allocation/
│   ├── metrics/
│   └── experiments/
│
├── experiments/
├── results/
│   ├── raw/
│   ├── processed/
│   └── figures/
│
├── tests/
├── docs/
│   ├── methodology.md
│   ├── experiments.md
│   └── system_design.md
│
├── main.py
├── requirements.txt
└── README.md
Research Direction

Future work can extend the framework with:

learned failure predictors
partially observable environments
decentralized communication
reinforcement learning
heterogeneous agents
stochastic failures
communication delays
larger-scale swarm experiments
statistical significance testing
hardware-in-the-loop validation
