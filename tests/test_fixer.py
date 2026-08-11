from jason.agents.fixer import Fixer


def test_fixer_run():

    fixer = Fixer()

    result = fixer.run(
        "Teste falhou: login não funciona"
    )

    assert result.status == "FIXED"
    assert result.error == "Teste falhou: login não funciona"
    assert result.action == "Correção aplicada"