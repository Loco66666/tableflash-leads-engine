from fastapi.testclient import TestClient

def test_create_and_list_restaurants(client: TestClient) -> None:
    user_response = client.post(
        "/api/v1/auth/users",
        json={
            "full_name": "Admin TFLE",
            "email": "admin@tableflash.test",
            "password": "secure-password-123",
        },
    )
    login_response = client.post(
        "/api/v1/auth/login",
        json={"email": "admin@tableflash.test", "password": "secure-password-123"},
    )
    headers = {"Authorization": f"Bearer {login_response.json()['access_token']}"}

    create_response = client.post(
        "/api/v1/restaurants",
        json={"name": "Le Bistrot TFLE", "city": "Bayonne"},
        headers=headers,
    )
    list_response = client.get("/api/v1/restaurants", headers=headers)

    assert user_response.status_code == 201
    assert login_response.status_code == 200
    assert create_response.status_code == 201
    assert create_response.json()["name"] == "Le Bistrot TFLE"
    assert list_response.status_code == 200
    assert [restaurant["name"] for restaurant in list_response.json()] == ["Le Bistrot TFLE"]
