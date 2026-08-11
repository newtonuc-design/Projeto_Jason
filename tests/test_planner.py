from jason.agents.planner import Planner


def test_planner_build():

    planner = Planner()

    plan = planner.build("Criar autenticação")

    assert plan.mission == "Criar autenticação"
    assert len(plan.steps) == 9
    assert plan.steps[0] == "Analisar missão"
    assert plan.steps[-1] == "Entregar"