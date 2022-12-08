import pytest
from main import app
from httpx import AsyncClient

nome = "Maria"
cpf = "999999999"
turma = "1"
idade = 42
global_response = []

@pytest.mark.asyncio
async def test_create_aluna():
    data = {
        "nome": nome,
        "cpf": cpf,
        "turma": turma,
        "idade": idade
    }
    async with AsyncClient(app=app, base_url="http://alunas") as ac:
        response = await ac.post("/alunas/", json=data) 
        global global_response 
        global_response = response
    assert response.status_code == 201 


@pytest.mark.asyncio
async def test_read_all_alunas():
    async with AsyncClient(app=app, base_url="http://alunas") as ac:
        response = await ac.get("/alunas/")
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_read_by_cpf_alunas():
    async with AsyncClient(app=app, base_url="http://alunas") as ac:
        response = await ac.get(f"/alunas/{cpf}")
    assert response.status_code == 200
        
# @pytest.mark.asyncio
# async def test_update_by_cpf_aluna():
#     data = {
#         "nome": nome,
#         "cpf": '1',
#         "turma": '130',
#         "idade": 42
#     }
#     async with AsyncClient(app=app, base_url="http://alunas") as ac:
#         response = await ac.put("/alunas/1", json=data)
#     assert response.status_code == 201


@pytest.mark.asyncio
async def test_update_by_id_aluna():
    data = {
        "nome": nome,
        "cpf": cpf,
        "turma": '130',
        "idade": 42
    }
    async with AsyncClient(app=app, base_url="http://alunas") as ac:
        response = await ac.put(f"/alunas/{global_response.json()['id']}", json=data)
    assert response.status_code == 200

@pytest.mark.asyncio
async def test_delete_by_cpf_alunas():
    async with AsyncClient(app=app, base_url="http://alunas") as ac:
        response = await ac.delete(f"/alunas/{cpf}")
    assert response.status_code == 204 
        