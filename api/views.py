from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Entry, User
from .serializers import EntrySerializer, UserSerializer
from .pagination import CustomPagination
from rest_framework.response import Response
from rest_framework import status


class EntryViewSet(ModelViewSet):
    queryset = Entry.objects.all().order_by('-created_at')
    serializer_class = EntrySerializer
    pagination_class = CustomPagination


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
