from django.shortcuts import render

from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse

from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # permission_classes = (AllowAny)
    serializer_class = RegisterSerializer


class DeleteUserView(APIView):

    def delete(self, request, pk):
        qs = User.objects.get(id=pk)
        qs.delete()
        return Response('User Deleted')


class RetrieveUserView(APIView):
    def get(self, request, *args, pk):
        qs = User.objects.get(id=pk)
        serializer = RegisterSerializer(qs, many=False)
        return Response(serializer.data)
