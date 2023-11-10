from rest_framework.serializers import ValidationError

from apphabits.models import habits


class habitsValidator:
    def __call__(self, value):
        nice_habit = value.nice_habit
        related_habit = value.related_habit
        reward = value.reward
        duration = value.duration
        period = value.period

        error=""
        #длительность <120
        if not nice_habit and duration > 120:
            error += "Длительность <120. "

        #период не реже чeм 1 раз в неделю
        if period.month:
            error += 'Раз в месяц нельзя только каждый день или раз в неделю. '

        # не может быть вознаграждения и связаной привычки
        if related_habit and reward:
            error += 'Не может быть вознаграждения и связаной привычки. '

        # Связаная привычка всегда приятная
        if related_habit:
            h_related_habit = habits.objects.get(pk=related_habit.id)
            if not h_related_habit.nice_habit:
                error += 'Связаная привычка всегда приятная. '

        # У приятной привычки нет вознаграждения
        if nice_habit and reward:
            error += "У приятной привычки нет вознаграждения. "


        if not error == '':
            raise ValidationError(error)