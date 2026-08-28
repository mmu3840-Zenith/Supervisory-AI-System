# System Architecture

```text
                  +----------------------+
                  |   Task Environment   |
                  +----------+-----------+
                             |
                             v
                  +----------------------+
                  |   Robot Agent Layer  |
                  +----------+-----------+
                             |
                             v
                  +----------------------+
                  | Failure Risk Model   |
                  +----------+-----------+
                             |
                             v
                  +----------------------+
                  | Supervisory Controller|
                  +----------+-----------+
                             |
                   +---------+---------+
                   |                   |
                   v                   v
            Continue Task       Redistribute
                                 Workload
                   |                   |
                   +---------+---------+
                             |
                             v
                  +----------------------+
                  |  Research Metrics    |
                  +----------------------+

The architecture separates:

agent autonomy
environment state
predictive risk estimation
centralized supervisory control
task allocation
quantitative evaluation
