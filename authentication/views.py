# views.py

from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from .serializers import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if not serializer.is_valid():
            return Response(
                {
                    'message': 'Registration failed due to validation errors',
                    'errors': serializer.errors,
                    'status': False
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        self.perform_create(serializer)
        
        username = serializer.validated_data.get('username')
        return Response({'message': f'Username {username} registered successfully','status': True},status=status.HTTP_201_CREATED)

class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BlogView(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = BlogSerializer
    def get_queryset(self):
        return Blog.objects.filter(User=self.request.user)
    def perform_create(self, serializer):
        serializer.save(User=self.request.user)