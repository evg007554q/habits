
from datetime import datetime, timedelta, timezone

from dateutil.relativedelta import relativedelta

import requests

from apphabits.models import habits
from config import settings




def app_send_message_tg(message_habits):
    """отправка сообщения """
    if message_habits.nice_habit:
        textm = f"А потом приятная привычка - {message_habits.action} в {message_habits.place}"
    else:
        textm = f"Напоминаю сейчас время - {message_habits.action} в {message_habits.place}"
    url = f"https://api.telegram.org/bot{settings.BOT_TG_TOKEN}/sendMessage?chat_id={settings.USER_TG_ID}&text={textm}"

    response = requests.get(url)

    if message_habits.reward:
        textm = f"Награда - {message_habits.reward} "
        url = f"https://api.telegram.org/bot{settings.BOT_TG_TOKEN}/sendMessage?chat_id={settings.USER_TG_ID}&text={textm}"
        response = requests.get(url)
    elif message_habits.related_habit:

        print(message_habits.related_habit.name)
        app_send_message_tg(message_habits.related_habit)


def app_send_message_schedule():
    """рассылка сообщений в телеграмме """


    for item_ms in habits.objects.all():
        # Если сейчас дата время больше даты отправки отправляем
        # После отправки переставляем дату время отправки вперед по расписанию
        # Текущая дата время
        d1 = datetime.now(timezone.utc)
        # item_ms.habits_time = d1
        # item_ms.save()


        if d1 > item_ms.habits_time and not item_ms.nice_habit:
            # /item_ms.habits_time:
            app_send_message_tg(item_ms)

            # каждый вторник во сколько-то или каждый месяц в указанный день
            # Определим дату следующей рассыки
            if item_ms.day == item_ms.period:
                # ежедневно
                # Сдвиг на один день
                dt_send=item_ms.habits_time + timedelta(days=1)

            elif item_ms.week == item_ms.period:
                # каждую неделю
                # Сдвиг на 7 деней
                dt_send = item_ms.habits_time + timedelta(days=7)

            elif item_ms.month:
                # каждый месяц
                # Сдвиг на месяц
                dt_send = (item_ms.habits_time + relativedelta(months=1))


            # print(dt_send)
            item_ms.habits_time = dt_send
            item_ms.save()





