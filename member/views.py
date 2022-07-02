from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import filters
from datetime import datetime
from django.contrib.humanize.templatetags.humanize import naturalday
from django.contrib.humanize.templatetags.humanize import naturaltime
from pspdfkit.init import single_certificate_gen

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


from .models import MemberProfile, AuthorAddress, ApplicationPayee,  ApplicationApproval, ApplicationReview
from .serializers import MemberProfileSerializer, AuthorAddressSerializer,ApplicationPayeeSerializer, ApplicationApprovalSerializer, ApplicationReviewSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['id'] = user.id
        token['is_staff'] = user.is_staff

        # token['profile_image'] = user.profile.profile_image
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/member/token',
        'member/token/refresh'
    ]
    return Response(routes)


##### MEMBER APP GET REQUESTS #####

# GET ALL MEMBERS

@api_view(['GET'])
def member_profile_list(request):
    if request.method == 'GET':
        qs = MemberProfile.objects.all().filter(user__is_staff =False).order_by('-created_at')
        serializer = MemberProfileSerializer(qs, many=True)
        return Response(serializer.data)

# GET MEMBER BY ID


@api_view(['GET'])
def member_profile_detail(request, pk):
    if request.method == 'GET':
        qs = MemberProfile.objects.get(id=pk)
        serializer = MemberProfileSerializer(qs)
        return Response(serializer.data)

@api_view(['GET'])
def member_certificate_gen(request, pk):
    if request.method == 'GET':
        qs = MemberProfile.objects.get(id=pk)
        name = str(qs.first_name + ' ' + qs.last_name)
        registration_certificate_picture = single_certificate_gen(name)
        print('registration_certificate_picture')
        print(registration_certificate_picture)
        qs.registration_certificate_picture = registration_certificate_picture
        qs.save()
        serializer = MemberProfileSerializer(qs)
        return Response(serializer.data)

@api_view(['GET'])
def member_confirm_payment(request, pk):
    if request.method == 'GET':
        member_profile = MemberProfile.objects.get(id=pk)
        member_profile.payment_confirmed = True
        member_profile.save()
        serializer = MemberProfileSerializer(member_profile)
        return Response(serializer.data)

# GET ALL ADDRESSES
@api_view(['GET'])
def member_address_list(request):
    if request.method == 'GET':
        qs = AuthorAddress.objects.all()
        serializer = AuthorAddressSerializer(qs, many=True)
        return Response(serializer.data)


# GET ADDRESS BY ID
@api_view(['GET'])
def member_address_detail(request, pk):
    if request.method == 'GET':
        qs = AuthorAddress.objects.get(id=pk)
        serializer = AuthorAddressSerializer(qs)
        return Response(serializer.data)




# GET ALL BOOK PAYEES
@api_view(['GET'])
def application_payee_list(request):
    if request.method == 'GET':
        qs = ApplicationPayee.objects.all()
        serializer = ApplicationPayeeSerializer(qs, many=True)
        return Response(serializer.data)

# ADD A BOOK FOR PUBLISH
@api_view(['POST'])
def addApplicationApproval(request):
    serializer = ApplicationApprovalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    else:
        return Response('serializer not valid')
    return Response(serializer.data)


# GET BOOK PAYEE BY ID
@api_view(['GET'])
def application_payee_detail(request, pk):
    if request.method == 'GET':
        qs = ApplicationPayee.objects.get(id=pk)
        serializer = ApplicationPayeeSerializer(qs)
        return Response(serializer.data)

# GET ALL BOOKS UNDER PUBLISH
@api_view(['GET'])
def application_approval_list(request):
    if request.method == 'GET':
        qs = ApplicationApproval.objects.all()
        print(qs)
        serializer = ApplicationApprovalSerializer(qs, many=True)
        return Response(serializer.data)


# GET BOOK UNDER PUBLISH BY ID
@api_view(['GET'])
def application_approval_detail(request, pk):
    if request.method == 'GET':
        qs = ApplicationApproval.objects.get(id=pk)
        serializer = ApplicationApprovalSerializer(qs)
        return Response(serializer.data)


# GET ALL BOOK REVIEWS
@api_view(['GET'])
def application_review_list(request):
    if request.method == 'GET':
        qs = ApplicationReview.objects.all()
        serializer = ApplicationReviewSerializer(qs, many=True)
        return Response(serializer.data)


# GET A REVIEW BY ID
@api_view(['GET'])
def application_review_detail(request, pk):
    if request.method == 'GET':
        qs = ApplicationReview.objects.get(id=pk)
        serializer = ApplicationReviewSerializer(qs)
        return Response(serializer.data)


# GET STORE BOOK BY ID
@api_view(['GET'])
def store_application_detail(request, pk):
    if request.method == 'GET':
        qs = StoreApplication.objects.get(id=pk)
        serializer = StoreApplicationSerializer(qs)
        return Response(serializer.data)

# GET ALL BLOG POST




##### MEMBER APP PATCH REQUESTS #####

class MemberProfileUpdate(APIView):
    def patch(self, request, pk):
        member_profile = MemberProfile.objects.get(id=pk)
        data = request.data

        member_profile.name = data.get('name', member_profile.name)
        member_profile.email = data.get('email', member_profile.email)
        member_profile.phone = data.get('phone', member_profile.phone)

        member_profile.save()
        serializer = MemberProfileSerializer(member_profile)
        return Response(serializer.data)

class MemberPaymentUpdate(APIView):
    def patch(self, request, pk):
        member_profile = MemberProfile.objects.get(id=pk)
        data = request.data

        member_profile.payment_confirmed = True
        member_profile.save()

        serializer = MemberProfileSerializer(member_profile)
        return Response(serializer.data)
class MemberProfilePictureUpdate(APIView):
    def patch(self, request, pk):
        member_profile = MemberProfile.objects.get(id=pk)
        data = request.data

        member_profile.profile_picture = data.get(
            'profile_picture', member_profile.profile_picture)

        member_profile.save()
        serializer = MemberProfileSerializer(member_profile)
        return Response(serializer.data)


class MemberAddressUpdate(APIView):
    def patch(self, request, pk):
        member_address = AuthorAddress.objects.get(id=pk)
        data = request.data

        member_address.building = data.get('building', member_address.building)
        member_address.street = data.get('street', member_address.street)
        member_address.city = data.get('city', member_address.city)
        member_address.country = data.get('country', member_address.country)
        member_address.postal_code = data.get(
            'postal_code', member_address.postal_code)
        member_address.isDefault = data.get(
            'isDefault', member_address.isDefault)

        member_address.save()
        serializer = AuthorAddressSerializer(member_address)
        return Response(serializer.data)


class ApplicationPayeeUpdate(APIView):
    def patch(self, request, pk):
        application_payee = ApplicationPayee.objects.get(id=pk)
        data = request.data

        application_payee.first_name = data.get('first_name', application_payee.first_name)
        application_payee.last_name = data.get('last_name', application_payee.last_name)
        application_payee.email = data.get('email', application_payee.email)
        application_payee.phone = data.get('phone', application_payee.phone)
        application_payee.paypal_email = data.get(
            'paypal_email', application_payee.paypal_email)
        application_payee.is_organization = data.get(
            'is_organization', application_payee.is_organization)

        application_payee.save()
        serializer = ApplicationPayeeSerializer(application_payee)
        return Response(serializer.data)


class ApplicationReviewUpdate(APIView):
    def patch(self, request, pk):
        application_review = ApplicationReview.objects.get(id=pk)
        data = request.data

        application_review.name = data.get('name', application_review.name)
        application_review.email = data.get('email', application_review.email)
        application_review.title = data.get('title', application_review.title)
        application_review.review = data.get('review', application_review.review)
        application_review.rating = data.get('rating', application_review.rating)
        application_review.is_approved = data.get(
            'is_approved', application_review.is_approved)

        application_review.save()
        serializer = ApplicationReviewSerializer(application_review)
        return Response(serializer.data)

class ApplicationApprovalUpdate(APIView):
    def patch(self, request, pk):
        application_approval = ApplicationApproval.objects.get(id=pk)
        data = request.data

        application_approval.title = data.get('title', application_approval.title)
        application_approval.description = data.get(
            'description', application_approval.description)
        application_approval.contributor_notes = data.get(
            'contributor_notes', application_approval.contributor_notes)
        application_approval.table_of_contents = data.get(
            'table_of_contents', application_approval.table_of_contents)
        application_approval.language = data.get('language', application_approval.language)
        application_approval.category = data.get('category', application_approval.category)
        application_approval.bisac_category1 = data.get(
            'bisac_category1', application_approval.bisac_category1)
        application_approval.bisac_category2 = data.get(
            'bisac_category2', application_approval.bisac_category2)
        application_approval.bisac_category3 = data.get(
            'bisac_category3', application_approval.bisac_category3)
        application_approval.keywords = data.get('keywords', application_approval.keywords)
        application_approval.audience = data.get('audience', application_approval.audience)
        application_approval.color = data.get('color', application_approval.color)
        application_approval.binding = data.get('binding', application_approval.binding)
        application_approval.paper = data.get('paper', application_approval.paper)
        application_approval.cover_finish = data.get(
            'cover_finish', application_approval.cover_finish)
        application_approval.isbn = data.get('isbn', application_approval.isbn)
        application_approval.pages = data.get('pages', application_approval.pages)
        application_approval.size = data.get('size', application_approval.size)
        application_approval.price = data.get('price', application_approval.price)
        application_approval.global_upload = data.get(
            'global_upload', application_approval.global_upload)
        application_approval.has_explicit_content = data.get(
            'has_explicit_content', application_approval.has_explicit_content)
        application_approval.is_active = data.get('is_active', application_approval.is_active)
        application_approval.is_banned = data.get('is_banned', application_approval.is_banned)
        application_approval.application_pdf = data.get('application_pdf', application_approval.application_pdf)

        application_approval.save()
        serializer = ApplicationApprovalSerializer(application_approval)
        return Response(serializer.data)


##### MEMBER APP DELETE REQUESTS #####


@api_view(['DELETE'])
def delete_member_profile(request, pk):
    member_profile = MemberProfile.objects.get(id=pk)
    member_profile.delete()
    return Response('Author profile deleted successfully')


@api_view(['DELETE'])
def delete_member_address(request, pk):
    member_address = AuthorAddress.objects.get(id=pk)
    member_address.delete()
    return Response('Author address deleted successfully')

@api_view(['DELETE'])
def delete_application_payee(request, pk):
    application_payee = ApplicationPayee.objects.get(id=pk)
    application_payee.delete()
    return Response('Application payee deleted successfully')


@api_view(['DELETE'])
def delete_application_review(request, pk):
    application_review = ApplicationReview.objects.get(id=pk)
    application_review.delete()
    return Response('Application review deleted successfully')

