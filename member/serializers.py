from rest_framework.serializers import ModelSerializer
from .models import MemberProfile, AuthorAddress, ApplicationPayee, ApplicationApproval, ApplicationReview
from django.contrib.auth.models import User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'

class MemberProfileSerializer(ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = MemberProfile
        fields = '__all__'

class AuthorAddressSerializer(ModelSerializer):
    class Meta:
        model = AuthorAddress
        fields = '__all__'

class ApplicationPayeeSerializer(ModelSerializer):
    class Meta:
        model = ApplicationPayee
        fields = '__all__'

class ApplicationReviewSerializer(ModelSerializer):
    class Meta:
        model = ApplicationReview
        fields = '__all__'


class ApplicationApprovalSerializer(ModelSerializer):
    class Meta:
        model = ApplicationApproval
        fields = '__all__'

