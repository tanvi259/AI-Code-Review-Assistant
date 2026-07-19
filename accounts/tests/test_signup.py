import pytest 
from rest_framework.test import APIClient
from django.contrib.auth.models import User 

@pytest.mark.django_db 
def test_signup():
    client = APIClient()
    
    data = {
        "username" : "testuser",
        "password" : "Test@123",
        "email" : "test@example.com"
    }

    response = client.post("/api/signup/", data, format="json")

    assert response.status_code == 201
    assert response.data["message"] == "User registered successfully"
    assert User.objects.filter(username="testuser").exists()