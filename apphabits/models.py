from django.db import models
from config import settings

class habits(models.Model):
    """ Привычки """
    name = models.CharField(max_length=100, verbose_name='Привычка')
    description = models.CharField(max_length=250, verbose_name='Описание Привычки', null=True, blank=True)
    habits_time = models.DateTimeField(verbose_name='время')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Создатель')
    action = models.CharField(max_length=250, verbose_name='Действие', null=True, blank=True)
    place = models.CharField(max_length=250, verbose_name='Место', null=True, blank=True)
    reward = models.CharField(max_length=250, verbose_name='Вознаграждение', null=True, blank=True)
    related_habit = models.ForeignKey(to='self', on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Связаная привычка')

    # периодичность каждый день/неделя/месяц
    # Например
    # каждый день 15:00 учить новое слово на англиском награда чашка кофе
    # Каждую метницу устраивать генеральную уборку награда выпить пива
    # Раз в месяц сходить в музей/выставка/театр награда посетить хорошее кафе
    day = "day"
    week = "week"
    month = "month"
    Mailing_schedule_ch=[
        (day, "Ежедневно"),
        (week, "Еженедельно"),
        (month, "Ежемесячно"),
    ]
    period = models.CharField(max_length=5, choices=Mailing_schedule_ch, default=day, verbose_name='Период ')

    nice_habit = models.BooleanField(default=False, verbose_name='Приятная привычка')
    public = models.BooleanField(default=False, verbose_name='Публичная привычка')
    duration = models.IntegerField(default=120, verbose_name='Длительность в секундах', null=True, blank=True)

    # start_of_habits = models.DateTimeField(verbose_name='Когда начали привыкать', null=True, blank=True)

    def __str__(self):
        return f'Привычка {self.name} выполняем {self.period} напомнить {self.habits_time}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ('habits_time',)