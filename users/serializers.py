from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer
from member.models import MemberProfile
import random
from django.core.exceptions import ObjectDoesNotExist
import numpy as np
from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'password','email')

    def create(self, validated_data):
        print("validated_data['password']", validated_data['password'])
        member_number = str(random_with_N_digits(4))
        member_registra_number = 'CSW' + member_number + '-2022'
        print('rand member_number', member_number)
        # data = np.random.randint(100,size=(12))
        # print('random data')
        # print(data)
        try:
            user = User.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = User.objects.create_user(**validated_data)
            member = MemberProfile(
                member_number = member_number,
                member_registra_number = member_registra_number,
                user = user,
                first_name =validated_data['first_name'],
                last_name =validated_data['last_name'],
                email =validated_data['email']
            )
            member.save()
        return user

