from jason.agents.executor import Executor


def test_executor_run():

    executor = Executor()

    log = executor.run([
        "Analisar missão",
        "Programar",
        "Executar pytest",
    ])

    assert log.status == "COMPLETED"
    assert len(log.completed) == 3
    assert log.completed[0] == "Analisar missão"
    assert log.completed[-1] == "Executar pytest"