"""Central supervisory decision layer."""

from __future__ import annotations

from dataclasses import dataclass

from src.agents.robot_agent import RobotAgent
from src.prediction.failure_predictor import predict_failure_risk


@dataclass
class SupervisorDecision:
    """Recorded supervisory decision."""

    agent_id: int
    risk: float
    action: str


class Supervisor:
    """Centralized supervisory controller."""

    def __init__(
        self,
        risk_threshold: float = 0.70,
    ) -> None:

        if not 0.0 <= risk_threshold <= 1.0:
            raise ValueError(
                "risk_threshold must be between 0 and 1"
            )

        self.risk_threshold = risk_threshold

    def assess(
        self,
        agent: RobotAgent,
    ) -> SupervisorDecision:
        """Assess one simulated agent."""

        risk = predict_failure_risk(
            energy=agent.energy,
            workload=agent.workload,
        )

        if risk >= self.risk_threshold:
            action = "redistribute"

        else:
            action = "continue"

        return SupervisorDecision(
            agent_id=agent.agent_id,
            risk=risk,
            action=action,
        )

    def assess_swarm(
        self,
        agents: list[RobotAgent],
    ) -> list[SupervisorDecision]:
        """Assess every active simulated agent."""

        return [
            self.assess(agent)
            for agent in agents
        ]
