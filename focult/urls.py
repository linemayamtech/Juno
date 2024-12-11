from django.urls import path
from .views import ComputerListView

urlpatterns = [
    path('api/computers/', ComputerListView.as_view(), name='computer-list'),
]
