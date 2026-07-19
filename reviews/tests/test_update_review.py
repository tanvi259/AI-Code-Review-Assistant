import pytest 
from unittest.mock import patch

from rest_framework.test import APIClient
from django.contrib.auth.models import User 

from reviews.models import CodeReview

@pytest.mark.django_db 
@patch("reviews.views.review_code")
def test_update_review(mock_review):

    mock_review.return_value = "Updated AI Review"

    user = User.objects.create_user(
        username="testuser",
        password="Test@123"
    )

    review = CodeReview.objects.create(
        user=user,
        language="Python",
        code="print('Hello World')",
        ai_review = "Old Review"
    )

    client = APIClient()

    response = client.post("/api/login/", {
        "username" : "testuser",
        "password" : "Test@123"
    },
    format="json")

    token = response.data["access"]

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    response=client.put(f"/api/updatereview/{review.id}/",
                        {
                            "language" : "Python",
                            "code" : "print('Updated')"
                        },
                        format="json")
    
    print(response.status_code)
    print(response.data)
    

    review.refresh_from_db()

    assert response.status_code == 200
    assert review.ai_review == "Updated AI Review"