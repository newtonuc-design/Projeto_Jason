from jason.agents.tester import Tester


def test_tester_run():

    tester = Tester()

    report = tester.run([
        "test_login",
        "test_logout",
        "test_register",
    ])

    assert report.status == "PASSED"

    assert len(report.executed) == 3

    assert report.executed[0] == "test_login"

    assert report.executed[-1] == "test_register"

    assert report.failed == []