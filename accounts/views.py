from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from accounts.serializers import UserSerializer


# Create your views here.
class RegisterView(generics.GenericAPIView):

    serializer_class = UserSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_data = serializer.data
            return Response(user_data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    