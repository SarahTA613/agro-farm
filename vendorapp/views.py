from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import VendorRegisterSerializer

# Create your views here.
class VendorRegisterView(APIView):

    def post(self,request):
        serializer = VendorRegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            # user=serializer.save()
            
            return Response({'msg': 'Registration Successul '},status=status.HTTP_201_CREATED)
            

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
