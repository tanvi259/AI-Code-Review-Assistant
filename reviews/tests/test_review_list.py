import pytest 
from rest_framework.test import APIClient

from django.contrib.auth.models import User

from reviews.models import CodeReview

@pytest.mark.django_db 
def test_review_list():

    user=User.objects.create_user(
        username="testuser",
        password="Test@123"
    )

    CodeReview.objects.create(
        user=user,
        language="Python",
        code="print('Hello)",
        ai_review="Good"
    )

    client = APIClient()

    response = client.post("/api/login/", {
        "username" : "testuser",
        "password" : "Test@123"
    },
    format="json")

    token = response.data["access"]

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    response = client.get("/api/reviewlist/")

    assert response.status_code == 200 
    assert len(response.data) == 1
    assert response.data[0]["language"] == "Python"