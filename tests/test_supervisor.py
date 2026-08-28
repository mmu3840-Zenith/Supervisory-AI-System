from src.agents.robot_agent import RobotAgent
from src.supervisor.supervisor import Supervisor


def test_supervisor_detects_high_risk():

    agent = RobotAgent(
        1,
        energy=10,
        workload=8,
    )

    supervisor = Supervisor(
        risk_threshold=0.70
    )

    decision = supervisor.assess(agent)

    assert decision.action == "redistribute"
    assert decision.risk >= 0.70
