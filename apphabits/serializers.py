from rest_framework import serializers

from apphabits.models import habits
from apphabits.validators import habitsValidator


class habitsSerializers(serializers.ModelSerializer):
    class Meta:
        model = habits
        fields = '__all__'

        validators = [
            habitsValidator(
                nice_habit='nice_habit',
                related_habit='related_habit',
                reward='reward',
                duration = 'duration',
                period = 'period')
        ]
