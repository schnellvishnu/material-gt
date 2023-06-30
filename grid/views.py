from django.shortcuts import render
from rest_framework import serializers
from rest_framework import viewsets
from .serializers import Data_tblSerializer
from .models import Data_tbl
# Create your views here.
class DataGridTableViewSet(viewsets.ModelViewSet):
    queryset =Data_tbl.objects.all()
    serializer_class =Data_tblSerializer