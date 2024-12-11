from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Computer
from .serializers import ComputerSerializer

class ComputerListView(APIView):
    """
    API endpoint to fetch all data from the Computer table.
    """
    def get(self, request):
        computers = Computer.objects.all()  # Fetch all records from the Computer table
        serializer = ComputerSerializer(computers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ComputerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)