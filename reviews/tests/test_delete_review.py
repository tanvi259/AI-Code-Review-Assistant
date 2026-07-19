import pytest

from rest_framework.test import APIClient
from django.contrib.auth.models import User

from reviews.models import CodeReview


@pytest.mark.django_db
def test_delete_review():

    user = User.objects.create_user(
        username="testuser",
        password="Test@123"
    )

    review = CodeReview.objects.create(
        user=user,
        language="Python",
        code="print('Hello')",
        ai_review="Good"
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

    response = client.delete(f"/api/deletereview/{review.id}/")

    assert response.status_code == 204
    assert CodeReview.objects.count() == 0