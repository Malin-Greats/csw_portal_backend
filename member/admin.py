from django.contrib import admin
from .models import MemberProfile, AuthorAddress, ApplicationPayee, ApplicationApproval, ApplicationReview


@admin.register(MemberProfile)
class MemberProfileAdmin(admin.ModelAdmin):
    search_fields = ("first_name",)

    list_display = ("id", "user","first_name","last_name", "email", "phone", "profile_picture",
                    "is_active", "is_banned", "created_at", "updated_at")


# @admin.register(AuthorAddress)
# class AuthorAddressAdmin(admin.ModelAdmin):
#     search_fields = ("name",)

#     list_display = ("id", "name", "building", "street", "city",
#                     "country", "postal_code", "isDefault", "created_at", "updated_at")


# @admin.register(ApplicationPayee)
# class ApplicationPayeeAdmin(admin.ModelAdmin):
#     search_fields = ("application",)

#     list_display = ("id", "member", "application", "first_name", "last_name", "email",
#                     "phone", "paypal_email", "is_organization", "created_at", "updated_at")


# @admin.register(ApplicationApproval)
# class ApplicationApprovalAdmin(admin.ModelAdmin):
#     search_fields = ("member",)
#     list_display = ("id", "member", "title", "description", "language", "category", "binding", "paper", "cover_finish", "application_pdf", "totalRevenue", "currentRevenue", "pages", "size", "price", "color",
#                     "bisac_category1", "bisac_category2", "keywords", "isbn", "cover", "global_upload", "has_explicit_content", "is_active", "is_banned", "created_at", "updated_at")


# @admin.register(ApplicationReview)
# class ApplicationReviewAdmin(admin.ModelAdmin):
#     search_fields = ("title",)
#     list_display = ("id", "name", "email", "application", "title",
#                     "review", "rating", "is_approved", "created_at", "updated_at")

