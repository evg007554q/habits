from rest_framework import serializers

from users.models import User
from apphabits.validators import habitsValidator


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'