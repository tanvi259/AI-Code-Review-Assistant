import pytest

from rest_framework.test import APIClient
from django.contrib.auth.models import User

from reviews.models import CodeReview


@pytest.mark.django_db
def test_single_review():

    user = User.objects.create_user(
        username="testuser",
        password="Test@123"
    )

    review = CodeReview.objects.create(
        user=user,
        language="Python",
        code="print('Hello World')",
        ai_review="Good Review"
    )

    client = APIClient()

    response = client.post(
        "/api/login/",
        {
            "username": "testuser",
            "password": "Test@123"
        },
        format="json"
    )

    token = response.data["access"]

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    response = client.get(f"/api/singlereview/{review.id}/")

    assert response.status_code == 200
    assert response.data["id"] == review.id
    assert response.data["language"] == "Python"
    assert response.data["code"] == "print('Hello World')"
    assert response.data["ai_review"] == "Good Review"