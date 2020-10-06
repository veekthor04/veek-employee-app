from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import redirect
from .models import Data
from .serializers import DataSerializer
import gspread
import os
import json

credentials_raw = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')

# Create your views here.
class DataList(generics.ListCreateAPIView):

    queryset = Data.objects.all()
    serializer_class = DataSerializer

class DataDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = Data.objects.all()
    serializer_class = DataSerializer

@api_view(['GET'])
def DataLoad(request, key):

    gc = gspread.service_account(json.loads(credentials_raw))
    try:
        sh = gc.open_by_key(key)
        worksheet = sh.sheet1
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    res = worksheet.get_all_records()
    for row in res:

        # Check if employee has not been added by checking employeeID 
        if not Data.objects.filter(employeeId=row['Employee ID']):
            employee = Data(firstName=row['First Name'],lastName=row['Last Name'],employeeId=row['Employee ID'],city=row['City'])
            employee.save()

    data = Data.objects.all()
    serializer = DataSerializer(data, many=True)

    return Response(serializer.data, status=status.HTTP_201_CREATED)

# 13yyd8s008LlRn0tn6LC5moH1fcBELBkYw2THX6gjdHU