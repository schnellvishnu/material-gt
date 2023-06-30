from rest_framework import serializers
from .models import Data_tbl


class Data_tblSerializer(serializers.ModelSerializer):
     class Meta:
         model=Data_tbl
         fields =['id','name','email','phone']