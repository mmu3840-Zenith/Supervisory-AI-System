from src.agents.robot_agent import RobotAgent


def test_agent_energy_is_bounded():
    agent = RobotAgent(1)

    agent.consume_energy(150)

    assert agent.energy == 0
    assert not agent.active


def test_agent_distance():
    agent = RobotAgent(
        1,
        x=0,
        y=0,
    )

    assert agent.distance_to((3, 4)) == 5
