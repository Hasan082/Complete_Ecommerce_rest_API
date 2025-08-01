from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "phone",
            "password",
            "confirm_password",
            "is_active",
            "is_staff",
        ]
        read_only_fields = ["id", "is_active", "is_staff"]

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError("Passwords do not match")
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        password = validated_data.pop("password")
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        
        password = validated_data.pop("password", None)
        confirm_password = validated_data.pop("confirm_password", None)
        
        if password is not None: # We can not check if password: empty string are falsy
            if password != confirm_password:
                raise serializers.ValidationError("Passwords do not match")
            instance.set_password(password)
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data['email']
        password = data['password']

        # Attempt to authenticate the user
        user = authenticate(email=email, password=password)

        if not user:
            raise serializers.ValidationError("Invalid credentials")
        
        return {'user': user}