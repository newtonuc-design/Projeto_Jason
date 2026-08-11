from jason.agents.software_engineer import SoftwareEngineer


def test_software_engineer_recebe_missao():
    engineer = SoftwareEngineer()

    result = engineer.execute(
        "Criar módulo de autenticação"
    )

    assert result.status == "COMPLETED"
    assert result.mission == "Criar módulo de autenticação"

    assert len(result.plan) == 9

    assert result.plan[0] == "Analisar missão"
    assert result.plan[-1] == "Entregar"

    assert result.actions == [
        "Missão recebida",
        "Planejamento concluído",
        "Execução concluída",
    ]

    assert result.tests == [
        "test_login",
        "test_logout",
        "test_register",
    ]

    assert result.result == "Missão executada com sucesso."