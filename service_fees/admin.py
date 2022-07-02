from django.contrib import admin
from .models import BindingOption, ApplicationSize, CoverFinish, InteriorColor, Page, PaperType


@admin.register(BindingOption)
class BindingOptionAdmin(admin.ModelAdmin):
    search_fields = ("id",)

    list_display = ("coil_bound", "hard_cover", "paper_back",
                    "saddle_stitch", "linen_wrap")


@admin.register(CoverFinish)
class CoverFinishAdmin(admin.ModelAdmin):
    search_fields = ("id",)

    list_display = ("glossy", "matte")


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    search_fields = ("id",)

    list_display = ("under50", "under100", "under200", "under300", "under400")


@admin.register(ApplicationSize)
class ApplicationSizeAdmin(admin.ModelAdmin):
    search_fields = ("id",)

    list_display = ("A4", "A5")


@admin.register(InteriorColor)
class InteriorColorAdmin(admin.ModelAdmin):
    search_fields = ("id",)

    list_display = ("black_white_prem", "black_white_stan",
                    "color_prem", "color_stan")


@admin.register(PaperType)
class PaperTypeAdmin(admin.ModelAdmin):
    search_fields = ("id",)

    list_display = ("cream", "white", "coated")
