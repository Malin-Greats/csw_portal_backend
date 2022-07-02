from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer
from member.models import MemberProfile
from django.core.exceptions import ObjectDoesNotExist

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'password','email')

    def create(self, validated_data):
        print("validated_data['password']", validated_data['password'])
        try:
            user = User.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:

            user = User.objects.create_user(**validated_data)
            member = MemberProfile(
                user = user,
                first_name =validated_data['first_name'],
                last_name =validated_data['last_name'],
                email =validated_data['email']
            )
            member.save()
        return user

