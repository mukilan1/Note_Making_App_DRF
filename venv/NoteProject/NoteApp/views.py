from django.shortcuts import render
from .serializers import CustomUserSerializer, NoteSerializer
from  django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import viewsets 
from django.shortcuts import get_object_or_404
from rest_framework import generics
import json
from .models import NoteModel
from rest_framework import permissions

User = get_user_model()

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer

class NoteViewSet(viewsets.ModelViewSet):
    queryset = NoteModel.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)