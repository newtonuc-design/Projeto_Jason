from fastapi.testclient import TestClient

from jason.api.main import app
from jason.api.routers.clientes import Cliente, clientes


client = TestClient(app)


def test_cadastrar_cliente_retorna_cliente_criado_com_status_201():
    quantidade_inicial = len(clientes)

    try:
        response = client.post(
            "/clientes",
            json={"nome": "Maria Souza", "telefone": "11999999999"},
        )

        assert response.status_code == 201
        assert response.json() == {
            "id": quantidade_inicial + 1,
            "nome": "Maria Souza",
            "telefone": "11999999999",
        }
        assert clientes[-1] == response.json()
    finally:
        if len(clientes) > quantidade_inicial:
            clientes.pop()


def test_cadastrar_cliente_rejeita_nome_ausente():
    response = client.post("/clientes", json={"telefone": "11999999999"})

    assert response.status_code == 422
    campos_com_erro = {erro["loc"][-1] for erro in response.json()["detail"]}
    assert campos_com_erro == {"nome"}


def test_cadastrar_cliente_rejeita_telefone_ausente():
    response = client.post("/clientes", json={"nome": "Maria Souza"})

    assert response.status_code == 422
    campos_com_erro = {erro["loc"][-1] for erro in response.json()["detail"]}
    assert campos_com_erro == {"telefone"}


def test_listar_clientes_retorna_objetos_compativeis_com_cliente():
    response = client.get("/clientes/")

    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert [Cliente(**cliente) for cliente in response.json()]
