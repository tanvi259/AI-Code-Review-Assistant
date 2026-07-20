# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializers import CodeReviewSerialzier

from .ai_service import review_code

from .models import CodeReview

from drf_yasg.utils import swagger_auto_schema

from django.shortcuts import render 

# Create your views here.
class SubmitCodeReviewAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=CodeReviewSerialzier,
        responses={201: CodeReviewSerialzier}
    )
    def post(self, request):
        serializer = CodeReviewSerialzier(data=request.data)

        if serializer.is_valid():
            language = serializer.validated_data["language"]
            code = serializer.validated_data["code"]

            try:
                ai_review = review_code(language, code)
            except Exception:
                ai_review = "AI review could not be generated at this time."

            serializer.save(
                user=request.user,
                ai_review=ai_review
            )

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        

# Get all previous reviews
class CodeReviewListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200:CodeReviewSerialzier(many=True)})
    def get(self,request):

        reviews = CodeReview.objects.filter(user=request.user).order_by("-created_at")

        serializer = CodeReviewSerialzier(
            reviews,
            many=True 
        )

        return Response(serializer.data)
    
# Get single review API
class CodeReviewDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200:CodeReviewSerialzier})
    def get(self,request,pk):

        review = get_object_or_404(CodeReview,id=pk,user=request.user)

        serializer = CodeReviewSerialzier(review)

        return Response(serializer.data)


# Update Review API
class CodeReviewUpdateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=CodeReviewSerialzier,
        responses={200: CodeReviewSerialzier}
    )
    def put(self, request, pk):
        review = get_object_or_404(
            CodeReview,
            id=pk,
            user=request.user
        )

        serializer = CodeReviewSerialzier(
            review,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            language = serializer.validated_data.get(
                "language",
                review.language
            )
            code = serializer.validated_data.get(
                "code",
                review.code
            )

            try:
                ai_review = review_code(language, code)
            except Exception:
                ai_review = "AI review could not be generated at this time."

            serializer.save(ai_review=ai_review)

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

#Delete Review API
class CodeReviewDeleteAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={204: "Review deleted successfully"})
    def delete(self,request,pk):
        review = get_object_or_404(CodeReview,id=pk,user=request.user)

        review.delete()

        return Response(
            {
                "message" : "Review deleted successfully"
            },
            status=status.HTTP_204_NO_CONTENT
        )
    
def home(request):
    return render(request, "reviews/home.html")