from rest_framework import serializers
from .models import CodeReview

class CodeReviewSerialzier(serializers.ModelSerializer):

    class Meta:
        model = CodeReview
        fields = ["id", "language", "code", "ai_review", "created_at", "updated_at"]
        read_only_fields = ["id", "ai_review", "created_at", "updated_at"]

        