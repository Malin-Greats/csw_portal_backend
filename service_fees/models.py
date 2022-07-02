from django.db import models


def upload_to(instance, filename):
    return filename.format(filename=filename)


# SERVICE FEES MODEL INTERIOR COLOR
class InteriorColor(models.Model):
    black_white_prem = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)  # premium
    black_white_stan = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)  # standard
    color_prem = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)  # premium
    color_stan = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)  # standard


# SERVICE FEES MODEL PAPER TYPE
class PaperType(models.Model):
    cream = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    white = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    coated = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)


# SERVICE FEES MODEL BINDING OPTIONS
class BindingOption(models.Model):
    coil_bound = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    hard_cover = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    paper_back = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    saddle_stitch = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    linen_wrap = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)


# SERVICE FEES MODEL COVER FINISH
class CoverFinish(models.Model):
    glossy = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    matte = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)


# SERVICE FEES MODEL PAGES
class Page(models.Model):
    under50 = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    under100 = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    under200 = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    under300 = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    under400 = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)


# SERVICE FEES MODEL BOOK SIZE
class ApplicationSize(models.Model):
    A4 = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
    A5 = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True, default=0)
