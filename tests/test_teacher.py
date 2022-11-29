def test_about_route(client):
    response = client.get("/users/1")
    assert response.status_code == 200
    assert b"Address" in response.data