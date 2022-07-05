from django.urls import path
from .views import MyTokenObtainPairView,MemberPaymentUpdate, MemberProfileUpdate, MemberProfilePictureUpdate, MemberAddressUpdate,  ApplicationApprovalUpdate,ApplicationPayeeUpdate, ApplicationReviewUpdate
from . import views

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [

    path('member-profile-list', views.member_profile_list,
         name='member-profile-list'),
    path('member-profile-detail/<str:user_id>', views.member_profile_detail,
         name='member-profile-detail'),
    path('member-certificate-gen/<str:user_id>', views.member_certificate_gen,
         name='member-certificate-gen'),
    path('member_confirm_payment/<str:user_id>', views.member_confirm_payment,
         name='member_confirm_payment'),
    path('member-address-list', views.member_address_list,
         name='member-address-list'),
    path('member-address-detail', views.member_address_detail,
         name='member-address-detail'),

    path('application-payee-list', views.application_payee_list, name='application-payee-list'),
    path('application-payee-detail', views.application_payee_detail, name='application-payee-detail'),

    path('application-approval-list', views.application_approval_list, name='application-approval-list'),
    path('application-approval-detail', views.application_approval_detail,
         name='application-approval-detail'),

    path('application-review-list', views.application_review_list, name='application-review-list'),
    path('application-review-detail', views.application_review_detail, name='application-review-detail'),

    path('member-profile-update/<str:user_id>',
         MemberProfileUpdate.as_view(), name='member-profile-update'),
    path('member-profile-picture-update/<str:user_id>',
         MemberProfilePictureUpdate.as_view(), name='member-profile-picture-update'),
    path('member-address-update/<str:user_id>',
         MemberAddressUpdate.as_view(), name='member-address-update'),
    path('application-approval-update/<str:user_id>',
         ApplicationApprovalUpdate.as_view(), name='application-approval-update'),
    path('application-payee-update/<str:user_id>',
         ApplicationPayeeUpdate.as_view(), name='application-payee-update'),
    path('application-review-update/<str:user_id>',
         ApplicationReviewUpdate.as_view(), name='application-review-update'),

    path('delete-member-profile/<str:user_id>',
         views.delete_member_profile, name='delete-member-profile'),
    path('delete-member-address/<str:user_id>',
         views.delete_member_address, name='delete-member-address'),
    path('delete-application-payee/<str:user_id>',
         views.delete_application_payee, name='delete-application-payee'),
    path('delete-application-review/<str:user_id>',
         views.delete_application_review, name='delete-application-review'),


    path('add-application-approval', views.addApplicationApproval, name="add-application-approval"),

    path('member_confirm_payment/', MemberPaymentUpdate.as_view(), name='member_confirm_payment'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
