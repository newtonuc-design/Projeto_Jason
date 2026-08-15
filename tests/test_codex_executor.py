import subprocess

from jason.executor import Executor
from jason.integrations.codex_executor import (
    CodexExecutor,
    build_codex_command,
    resolve_codex_command,
)


def test_build_codex_command_keeps_command_construction_separate():
    assert build_codex_command("implemente a tarefa") == [
        "codex",
        "exec",
        "implemente a tarefa",
    ]


def test_codex_executor_implements_executor_contract():
    assert isinstance(CodexExecutor(), Executor)


def test_resolve_codex_command_uses_npm_cmd_launcher_on_windows():
    lookups = []

    def which(executable):
        lookups.append(executable)
        return r"C:\npm\codex.cmd"

    command = resolve_codex_command(
        ["codex", "exec", "implemente a tarefa"], os_name="nt", which=which
    )

    assert command == [r"C:\npm\codex.cmd", "exec", "implemente a tarefa"]
    assert lookups == ["codex.cmd"]


def test_resolve_codex_command_keeps_codex_name_on_other_systems():
    command = resolve_codex_command(
        ["codex", "exec", "implemente a tarefa"],
        os_name="posix",
        which=lambda executable: r"C:\npm\codex.cmd",
    )

    assert command == ["codex", "exec", "implemente a tarefa"]


def test_resolve_codex_command_keeps_custom_executable_on_windows():
    command = resolve_codex_command(
        ["custom-codex", "--prompt", "tarefa"],
        os_name="nt",
        which=lambda executable: r"C:\npm\codex.cmd",
    )

    assert command == ["custom-codex", "--prompt", "tarefa"]


def test_executor_runs_command_from_configured_builder_and_returns_process_output():
    calls = []

    def command_builder(instruction):
        return ["custom-codex", "--prompt", instruction]

    def runner(command, **kwargs):
        calls.append((command, kwargs))
        return subprocess.CompletedProcess(command, 7, stdout="saida", stderr="erro")

    result = CodexExecutor(command_builder, runner=runner).execute("faça a revisão")

    assert calls == [
        (
            ["custom-codex", "--prompt", "faça a revisão"],
            {"capture_output": True, "text": True, "check": False},
        )
    ]
    assert result.stdout == "saida"
    assert result.stderr == "erro"
    assert result.returncode == 7
