from rest_framework import generics
from .models import Paste
from django.contrib.auth.models import User
from .serializers import PasteSerializer, UserSerializer
from rest_framework import permissions


class PasteList(generics.ListCreateAPIView):
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PasteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paste.objects.all()
    serializer_class = PasteSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
