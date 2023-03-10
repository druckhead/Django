from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import BooleanField
from rest_framework.validators import UniqueValidator


class UserResgisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "confirm_password",
        ]
        extra_kwargs = {
            "first_name": {
                "required": True,
            },
            "last_name": {
                "required": True,
            },
            "email": {
                "required": True,
                "validators": [
                    UniqueValidator(queryset=User.objects.all()),
                ],
            },
            "password": {
                "write_only": True,
                "required": True,
            },
            "confirm_password": {
                "write_only": True,
                "required": True,
            },
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise ValidationError({"password": "Password Fields must match."})
        try:
            validate_password(attrs["password"])
        except ValidationError as validerr:
            raise serializers.ValidationError({"password": validerr})

        return attrs

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user


class StaffRegisterSerializer(UserResgisterSerializer):
    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "confirm_password",
            "is_staff",
        ]
        extra_kwargs = {
            "first_name": {
                "required": True,
            },
            "last_name": {
                "required": True,
            },
            "email": {
                "required": True,
                "validators": [
                    UniqueValidator(queryset=User.objects.all()),
                ],
            },
            "password": {
                "write_only": True,
                "required": True,
            },
            "confirm_password": {
                "write_only": True,
                "required": True,
            },
            "is_staff": {"default": True},
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise ValidationError({"password": "Password Fields must match."})
        try:
            validate_password(attrs["password"])
        except ValidationError as validerr:
            raise serializers.ValidationError({"password": validerr})

        return attrs

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            is_staff=validated_data["is_staff"],
        )
        user.set_password(validated_data["password"])
        user.save()

        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password"]
