from rest_framework import generics

from apphabits.models import habits
from apphabits.paginators import apphabitsPaginator
from apphabits.permissions import IsOwner
from apphabits.serializers import habitsSerializers


class  habitsCreateAPIView(generics.CreateAPIView):
    serializer_class = habitsSerializers

    #Авторизован и группа IsMember
    def perform_create(self, serializer_class):
        newS = serializer_class.save()
        newS.owner = self.request.user
        newS.save()

class habitsListAPIView(generics.ListAPIView):
    serializer_class = habitsSerializers
    queryset = habits.objects.all()
    permission_classes = [IsOwner]
    pagination_class = apphabitsPaginator

class habits_publicListAPIView(generics.ListAPIView):
    serializer_class = habitsSerializers
    queryset = habits.objects.all(public=True)
    pagination_class = apphabitsPaginator

class habitsDestroyAPIView(generics.DestroyAPIView):
    queryset = habits.objects.all()
    permission_classes = [IsOwner]
