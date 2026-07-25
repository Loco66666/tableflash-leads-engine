from fastapi.testclient import TestClient

def test_create_and_list_restaurants(client: TestClient) -> None:

    create_response = client.post(
        "/api/v1/restaurants",
        json={"name": "Le Bistrot TFLE", "city": "Bayonne"},
    )
    list_response = client.get("/api/v1/restaurants")

    assert create_response.status_code == 201
    assert create_response.json()["name"] == "Le Bistrot TFLE"
    assert list_response.status_code == 200
    assert [restaurant["name"] for restaurant in list_response.json()] == ["Le Bistrot TFLE"]
