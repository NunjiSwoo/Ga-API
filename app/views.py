from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import SensorData
from .serializers import SensorDataSerializer

def umnomepraele(request):
    
    return render(request, "a.html")

class SensorDataAPIView(APIView):
    def get(self, request):
        data = SensorData.objects.all()
        serializer = SensorDataSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SensorDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Sensor data created successfully" if serializer.instance else "Sensor data updated successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)