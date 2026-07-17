
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import SignupSerialzier, LoginSerializer

from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class SignupAPIView(APIView):

    @swagger_auto_schema(request_body=SignupSerialzier,responses={201:"User created successfully"})
    def post(self,request):
        serializer = SignupSerialzier(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {
                    "message" : "User registered successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class LoginAPIView(APIView):
    @swagger_auto_schema(request_body=LoginSerializer,responses={201:LoginSerializer})
    def post(self,request):
        serializer = LoginSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.validated_data["user"]

            refresh = RefreshToken.for_user(user)
            access = refresh.access_token

            return Response(
                {
                    "message" : "Login Successful",
                    "access" : str(access),
                    "refresh" : str(refresh),
                },
                status=status.HTTP_200_OK
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST

        )

