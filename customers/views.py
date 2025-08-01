from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from customers.models import CustomUser
from customers.serializers import CustomUserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class LoginView(APIView):
    def post(self, request):
        # Deserialize and validate the data
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.validated_data.get('user')  # Extract user from validated data

            # Ensure the user object is valid
            if user is None:
                return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

            # Create the JWT tokens
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token

            return Response(
                {
                    'refresh': str(refresh),
                    'access': str(access_token)
                },
                status=status.HTTP_200_OK
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if hasattr(request.user, "auth_token"):
            request.user.auth_token.delete()
        return Response(
            {"message": "Logged out successfully"}, status=status.HTTP_200_OK
        )
