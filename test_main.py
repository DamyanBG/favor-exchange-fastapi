from fastapi.testclient import TestClient
import pytest

from main import app
from schemas.reguest.user import UserRegisterIn
from resources.user_route import create_user

client = TestClient(app)


def test_read_main():
    response = client.get("/works/")
    assert response.status_code == 200
    assert response.json() == "works"


def test_registers(mocker):
    mock_database = mocker.patch("managers.users_manager.UserManager.register")
    mock_database.return_value = "gfj83429fh34ehui8"

    post_dict: UserRegisterIn = {
        "first_name": "Dimitar",
        "last_name": "Dimitrov",
        "email": "2323@abv.bg",
        "password": "123432523535",
        "phone": "2141242234",
    }

    response = client.post(url="/users/", json=post_dict)

    assert response.json() == {"token": "gfj83429fh34ehui8"}


@pytest.mark.asyncio
async def test_register(mocker):
    mock_database = mocker.patch("managers.users_manager.UserManager.register")
    mock_database.return_value = "gfj83429fh34ehui8"

    post_dict = {
        "first_name": "Dimitar",
        "last_name": "Dimitrov",
        "email": "2323@abv.bg",
        "password": "123432523535",
        "phone": "2141242234",
    }

    post_object = UserRegisterIn(**post_dict)
    result = await create_user(post_object)

    assert result == {"token": "gfj83429fh34ehui8"}
