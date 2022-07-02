from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics
from django.http import JsonResponse


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import filters
from datetime import datetime


from .models import BindingOption, ApplicationSize, CoverFinish, InteriorColor, Page, PaperType
from .serializers import BindingOptionSerializer, ApplicationSizeSerializer, CoverFinishSerializer, InteriorColorSerializer, PageSerializer, PaperTypeSerializer


##### SERVICE FEES APP GET REQUESTS #####

# GET ALL INTERIOR COLORS

@api_view(['GET'])
def interior_colors_list(request):
    if request.method == 'GET':
        qs = InteriorColor.objects.all()
        serializer = InteriorColorSerializer(qs, many=True)
        return Response(serializer.data)


# GET ALL PAPER TYPE

@api_view(['GET'])
def paper_type_list(request):
    if request.method == 'GET':
        qs = PaperType.objects.all()
        serializer = PaperTypeSerializer(qs, many=True)
        return Response(serializer.data)


# GET ALL BINDING OPTIONS

@api_view(['GET'])
def binding_options_list(request):
    if request.method == 'GET':
        qs = BindingOption.objects.all()
        serializer = BindingOptionSerializer(qs, many=True)
        return Response(serializer.data)


# GET ALL PAPER TYPE

@api_view(['GET'])
def cover_finish_list(request):
    if request.method == 'GET':
        qs = CoverFinish.objects.all()
        serializer = CoverFinishSerializer(qs, many=True)
        return Response(serializer.data)


# GET ALL PAGES

@api_view(['GET'])
def pages_list(request):
    if request.method == 'GET':
        qs = Page.objects.all()
        serializer = PageSerializer(qs, many=True)
        return Response(serializer.data)


# GET ALL BOOK SIZE

@api_view(['GET'])
def application_size_list(request):
    if request.method == 'GET':
        qs = ApplicationSize.objects.all()
        serializer = ApplicationSizeSerializer(qs, many=True)
        return Response(serializer.data)


##### SERVICE FEES APP PATCH REQUESTS #####

class InteriorColorUpdate(APIView):
    def patch(self, request, pk):
        qs = InteriorColor.objects.get(id=pk)
        data = request.data

        qs.black_white_prem = data.get('black_white_prem', qs.black_white_prem)
        qs.black_white_stan = data.get('black_white_stan', qs.black_white_stan)
        qs.color_prem = data.get('color_prem', qs.color_prem)
        qs.color_stan = data.get('color_stan', qs.color_stan)

        qs.save()
        serializer = InteriorColorSerializer(qs)
        return Response(serializer.data)


class PaperTypeUpdate(APIView):
    def patch(self, request, pk):
        qs = PaperType.objects.get(id=pk)
        data = request.data

        qs.cream = data.get('cream', qs.cream)
        qs.white = data.get('white', qs.white)
        qs.coated = data.get('coated', qs.coated)

        qs.save()
        serializer = PaperTypeSerializer(qs)
        return Response(serializer.data)


class BindingOptionUpdate(APIView):
    def patch(self, request, pk):
        qs = BindingOption.objects.get(id=pk)
        data = request.data

        qs.coil_bound = data.get('coil_bound', qs.coil_bound)
        qs.hard_cover = data.get('hard_cover', qs.hard_cover)
        qs.paper_back = data.get('paper_back', qs.paper_back)
        qs.saddle_stitch = data.get('saddle_stitch', qs.saddle_stitch)
        qs.linen_wrap = data.get('linen_wrap', qs.linen_wrap)

        qs.save()
        serializer = BindingOptionSerializer(qs)
        return Response(serializer.data)


class CoverFinishUpdate(APIView):
    def patch(self, request, pk):
        qs = CoverFinish.objects.get(id=pk)
        data = request.data

        qs.glossy = data.get('glossy', qs.glossy)
        qs.matte = data.get('matte', qs.matte)

        qs.save()
        serializer = CoverFinishSerializer(qs)
        return Response(serializer.data)


class PageUpdate(APIView):
    def patch(self, request, pk):
        qs = Page.objects.get(id=pk)
        data = request.data

        qs.under50 = data.get('under50', qs.under50)
        qs.under100 = data.get('under100', qs.under100)
        qs.under200 = data.get('under200', qs.under200)
        qs.under300 = data.get('under300', qs.under300)
        qs.under400 = data.get('under400', qs.under400)

        qs.save()
        serializer = PageSerializer(qs)
        return Response(serializer.data)


class ApplicationSizeUpdate(APIView):
    def patch(self, request, pk):
        qs = ApplicationSize.objects.get(id=pk)
        data = request.data

        qs.A4 = data.get('A4', qs.A4)
        qs.A5 = data.get('A5', qs.A5)

        qs.save()
        serializer = ApplicationSizeSerializer(qs)
        return Response(serializer.data)
