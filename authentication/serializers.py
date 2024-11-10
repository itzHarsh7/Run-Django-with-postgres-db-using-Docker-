from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import *
from rest_framework import serializers

class UserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'confirm_password', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.get('confirm_password')
        if password != confirm_password:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        return attrs

    def create(self, validated_data):
        validated_data.pop('confirm_password', None)
        user = User.objects.create_user(**validated_data)
        default_role, created = Role.objects.get_or_create(name="EndUser")
        user.role = default_role
        user.save()
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'),email=email, password=password)

        if not user:
            raise serializers.ValidationError("Incorrect Credentials")

        # Check if the user already has an associated token
        token, created = Token.objects.get_or_create(user=user)
        
        return {
            'user': user,
            'token': token.key  # Return the token key
        }
    def to_representation(self, instance):
        """Override this method to format the output response"""
        # Return data with the necessary fields
        print('instance--> ', instance)
        user_data = {
            'email': instance['user'].email,
            'username': instance['user'].username,
            'role': instance['user'].role.name,
            'first_name': instance['user'].first_name,
            'last_name': instance['user'].last_name,
        }
        return {
            'message': 'Login Successfull',
            'data': user_data,
            'token': instance['token'],
            'status':True
        }
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['blogid','title','content']
        read_only_fields = ['blogid']