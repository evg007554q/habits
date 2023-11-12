from rest_framework.serializers import ValidationError

from apphabits.models import habits


class habitsValidator:
    def __init__(self, nice_habit,  related_habit, reward, duration, period ):
        self.nice_habit = nice_habit
        self.related_habit = related_habit
        self.reward = reward
        self.duration = duration
        self.period = period

    def __call__(self, value):


        nice_habit = dict(value).get( 'nice_habit')
        related_habit = dict(value).get( 'related_habit')
        reward = dict(value).get( 'reward')
        duration = dict(value).get( 'duration')
        period = dict(value).get( 'period')

        error=""
        #длительность <120
        if not nice_habit and duration > 120:
            error += "Длительность <120. "

        #период не реже чeм 1 раз в неделю
        if period == 'month':
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

        print(error)
        if not error == '':
            raise ValidationError(error)