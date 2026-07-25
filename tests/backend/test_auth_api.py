from fastapi.testclient import TestClient


def create_bootstrap_admin(client: TestClient) -> dict[str, object]:
    response = client.post(
        "/api/v1/auth/users",
        json={
            "full_name": "Admin TFLE",
            "email": "admin@tableflash.test",
            "password": "secure-password-123",
            "role": "commercial",
        },
    )
    assert response.status_code == 201
    return response.json()


def login(client: TestClient) -> str:
    response = client.post(
        "/api/v1/auth/login",
        json={"email": "admin@tableflash.test", "password": "secure-password-123"},
    )
    assert response.status_code == 200
    return response.json()["access_token"]


def test_bootstrap_login_and_current_user(client: TestClient) -> None:
    user = create_bootstrap_admin(client)
    token = login(client)

    me_response = client.get("/api/v1/auth/me", headers={"Authorization": f"Bearer {token}"})

    assert user["role"] == "admin"
    assert me_response.status_code == 200
    assert me_response.json()["email"] == "admin@tableflash.test"


def test_only_an_admin_can_create_later_users(client: TestClient) -> None:
    create_bootstrap_admin(client)

    forbidden_response = client.post(
        "/api/v1/auth/users",
        json={
            "full_name": "Commercial TFLE",
            "email": "commercial@tableflash.test",
            "password": "secure-password-456",
        },
    )
    token = login(client)
    allowed_response = client.post(
        "/api/v1/auth/users",
        headers={"Authorization": f"Bearer {token}"},
        json={
            "full_name": "Commercial TFLE",
            "email": "commercial@tableflash.test",
            "password": "secure-password-456",
            "role": "commercial",
        },
    )

    assert forbidden_response.status_code == 403
    assert allowed_response.status_code == 201
    assert allowed_response.json()["role"] == "commercial"


def test_restaurant_routes_require_a_valid_token(client: TestClient) -> None:
    unauthenticated_response = client.get("/api/v1/restaurants")
    create_bootstrap_admin(client)
    token = login(client)
    authenticated_response = client.get(
        "/api/v1/restaurants", headers={"Authorization": f"Bearer {token}"}
    )

    assert unauthenticated_response.status_code == 401
    assert authenticated_response.status_code == 200
