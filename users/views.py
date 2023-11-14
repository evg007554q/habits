
from rest_framework import generics

from users.serializers import UsersSerializers


class  UsersCreateAPIView(generics.CreateAPIView):
    serializer_class = UsersSerializers

    def perform_create(self, serializer_class):
        newS = serializer_class.save()


