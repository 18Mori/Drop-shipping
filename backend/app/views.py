from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from .models import *
from django.utils import timezone
from rest_framework.views import APIView


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        user = serializer.save()
        profile, created = UserProfile.objects.get_or_create(user=user)
        if created:
            print(f"✅ UserProfile created for {user.username}")
        
class UserListView(generics.ListAPIView):
    queryset = User.objects.all().prefetch_related('notes').select_related('profile')
    serializer_class = UserDetailedSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        print(f"📊 Returning {len(response.data)} users")
        for user_data in response.data:
            print(f"   User: {user_data['username']}, Notes: {user_data['notes_count']}, Active: {user_data['is_currently_active']}")
        return response

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all().prefetch_related('notes').select_related('profile')
    serializer_class = UserDetailedSerializer
    permission_classes = [IsAuthenticated]
    
    lookup_field = "id"
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        user_data = response.data
        print(f"👤 User Detail: {user_data['username']}")
        print(f"   Notes: {user_data['notes']}")
        print(f"   Profile: {user_data['profile']}")
        return response

class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailedSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = "id"
    
class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            note = serializer.save(author=self.request.user)
            print(f"✅ Note created: {note.title} by {self.request.user.username}")
        else:
            print(serializer.errors)
            
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=self.request.user)

class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=self.request.user)

class CurrentUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        serializer = UserDetailedSerializer(request.user)
        return Response(serializer.data)