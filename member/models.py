import queue
from sre_parse import WHITESPACE
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta


def upload_to(instance, filename):
    return filename.format(filename=filename)


# MEMBER'S PROFILE MODEL
class MemberProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=150)
    phone = models.CharField(max_length=100)
    profile_picture = models.ImageField(
        upload_to=upload_to, blank=True, null=True)
    registration_certificate_picture = models.ImageField(
        upload_to=upload_to, blank=True, null=True)
    practicing_certificate_picture = models.ImageField(
        upload_to=upload_to, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_banned = models.BooleanField(default=False)
    payment_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.first_name

# RECEIVER TO TRIGGER CREATION OF PROFILE AFTER NEW USER IS CREATED


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     print('instance', sender)

#     if created:
#         pass
#     else:
#         instance.profile.save()


# MEMBER ADDRESS MODEL
class AuthorAddress(models.Model):
    name = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    building = models.CharField(max_length=200, null=True, blank=True)
    street = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    # state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(
        max_length=25, default=0000, null=True, blank=True)
    isDefault = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

# BOOK FOR PUBLISH  MODEL
class ApplicationApproval(models.Model):
    member = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True,
                             blank=True, default="title")
    description = models.TextField(
        max_length=1000, null=True, blank=True, default="description")
    approver_notes = models.TextField(
        max_length=1000, null=True, blank=True, default="approver_notes")
    language = models.CharField(
        max_length=200, null=True, blank=True, default="language")

    certificate_pdf = models.FileField(upload_to=upload_to, null=True, blank=True)
    global_access = models.BooleanField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    is_active = models.BooleanField(default=True, null=True, blank=True)
    is_paid = models.BooleanField(default=True, null=True, blank=True)
    is_banned = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created_at',)


# BOOK PAYEE MODEL **works only on approvaled applications
class ApplicationPayee(models.Model):
    member = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    application = models.ForeignKey(ApplicationApproval, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    paypal_email = models.EmailField(max_length=150, blank=True, null=True)
    payment_txn_id = models.CharField(
        max_length=200, null=True, blank=True, default="payment_txn_id")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name


# BOOK REVIEW MODEL **works only on approvaled applications in the store
class ApplicationReview(models.Model):
    # member = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    reviewer_id = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=150, blank=True, null=True)
    application = models.ForeignKey(ApplicationApproval, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True, null=True)
    review = models.TextField(max_length=1000, null=True, blank=True)
    rating = models.IntegerField(default=0, blank=True, null=True)
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
