import pytest
from unittest.mock import patch 

from rest_framework.test import APIClient
from django.contrib.auth.models import User 

from reviews.models import CodeReview 

@pytest.mark.django_db 
@patch("reviews.views.review_code")
def test_submit_review(mock_review):

    mock_review.return_value = "Mock AI Review"

    User.objects.create_user(
        username = "testuser",
        password = "Test@123"
    )

    client = APIClient()

    data = {
        "username" : "testuser",
        "password" : "Test@123"
    }
    response = client.post("/api/login/",data, response="json")

    token = response.data["access"]

    client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    resposne = client.post("/api/submitreview/",
                           {
                               "language" : "Python",
                               "code" : "print('Hello World')"
                           },
                           format="json")

    assert resposne.status_code == 201 
    assert resposne.data["ai_review"] == "Mock AI Review"
    assert CodeReview.objects.count() == 1