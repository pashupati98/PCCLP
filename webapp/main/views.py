# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic.base import View
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from .feature_extractor import *
from .script import *
import pickle
import math

# loaded_model = pickle.load(open('m .models/model_v3.0.pkl', "rb"))


class Run(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        ans = ValuePredictor(feature_extractor([request.POST['repunit']]))

        return Response(
            #feature_extractor(list(request.POST['repunit'])),
            # feature_extractor([request.POST['repunit']]),
            ans,
            # request.POST['repunit'],
            status=status.HTTP_200_OK
        )


class UI(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'ui1.html', context=None, content_type=None, status=None, using=None)
