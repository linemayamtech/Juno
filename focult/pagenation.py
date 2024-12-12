# pagination.py
from rest_framework.pagination import PageNumberPagination

class ComputerPagination(PageNumberPagination):
    page_size = 10  # Default number of records per page
    page_size_query_param = 'page_size'  # Allow clients to set the page size
    max_page_size = 100  # Limit the maximum page size
