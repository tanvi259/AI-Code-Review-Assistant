import pytest 
from rest_framework.test import APIClient
from django.contrib.auth.models import User 

@pytest.mark.django_db
def test_login():
    client = APIClient()

    User.objects.create_user(
        username="testuser",
        email="test@example.com",
        password="Test@123"
    )

    data = {
        "username" : "testuser",
        "password" : "Test@123"
    }

    response = client.post("/api/login/", data, format="json")

    assert response.status_code == 200
    assert response.data["message"] == "Login Successful"
    assert "access" in response.data
    assert "refresh" in response.data

