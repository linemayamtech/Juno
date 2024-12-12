# views.py
from rest_framework.pagination import PageNumberPagination
from .pagenation import ComputerPagination  # Import the custom pagination class
from .models import Computer
from .serializers import ComputerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ComputerListView(APIView):
    """
    API endpoint to fetch and create Computers with pagination.
    """
    def get(self, request):
        computers = Computer.objects.all().order_by('-c_log_ts')  # Fetch all records ordered by latest timestamp
        
        # Apply pagination
        paginator = ComputerPagination()
        paginated_computers = paginator.paginate_queryset(computers, request)
        
        # Serialize the paginated data
        serializer = ComputerSerializer(paginated_computers, many=True)
        
        # Return paginated response
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = ComputerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
