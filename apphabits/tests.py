from django.test import TestCase

# Create your tests here.
from rest_framework.test import APITestCase, APIClient

from apphabits.models import habits
from users.models import User
from datetime import datetime, timedelta, timezone
from django.urls import reverse
from rest_framework import status

class habitsTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(
            email='user@test.com',
            password='test_password'
        )
        self.client.force_authenticate(user=self.user)


        # d1 = datetime.now(timezone.utc)
        self.data = habits.objects.create(
            name='Привычка',
            habits_time='2023-11-11T00:00:00Z',
            owner=self.user,
            action='Действие',
            place='Место',
            reward='Вознаграждение',
            period='day',
            nice_habit=False,
            public=False,
            duration=60,

        )
        # related_habit = 'Связаная привычка'


    def test_get_list(self):
        """Список - Привычки"""
        response = self.client.get(
            '/habits/'
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
        # print(response.json())
        self.assertEquals(
            response.json(),
            {'count': 1, 'next': None, 'previous': None, 'results': [
                {'id': 1, 'name': 'Привычка', 'description': None, 'habits_time': '2023-11-11T00:00:00Z',
                 'action': 'Действие', 'place': 'Место', 'reward': 'Вознаграждение', 'period': 'day',
                 'nice_habit': False, 'public': False, 'duration': 60, 'owner': 1, 'related_habit': None}]}

        )


    def test_get_public_list(self):
        """Список - Привычки - public"""
        response = self.client.get(
            '/habits_public/'
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEquals(
            response.json(),
            {'count': 0, 'next': None, 'previous': None, 'results': []
             }

        )

    def test_validation_habits1(self):
        """добавление плохой привычки1"""
        # self.data.save()
        self.client.force_authenticate(user=self.user)
        data = { 'name': 'Привычка', 'habits_time': '2023-11-11 00:00:00',
                'action': 'Действие', 'place': 'Место', 'reward': 'Вознаграждение', 'period': 'day',
                'nice_habit': False, 'public': False, 'duration': 160}


        response = self.client.post(
            '/habits/create/',
            data=data
        )
        self.assertEquals(response.json(), {'non_field_errors': ['Длительность <120. ']})

    def test_validation_habits2(self):
        """добавление плохой привычки2"""
        # self.habits.save()
        # self.data.refresh_from_db()
        self.client.force_authenticate(user=self.user)

        data1 = habits.objects.create(
            id= 33,
            name='Привычка',
            habits_time='2023-11-11T00:00:00Z',
            owner=self.user,
            action='Действие',
            place='Место',
            reward='Вознаграждение',
            period='day',
            nice_habit=True,
            public=False,
            duration=60,
        )
        data1.refresh_from_db()

        data2= {'name': 'Привычка', 'habits_time': '2023-11-11 00:00:00',
                 'action': 'Действие', 'place': 'Место', 'reward': 'Вознаграждение', 'period': 'day',
                 'nice_habit': False, 'public': False, 'duration': 120, 'related_habit': 33}


        response = self.client.post(
            '/habits/create/',
            data=data2
        )
        print(response.json())
        self.assertEquals(response.json(),
        {'non_field_errors':
             ['Не может быть вознаграждения и связаной привычки. ']
         })


    def test_validation_habits3(self):
        """добавление плохой привычки2"""
        # self.habits.save()
        # self.data.refresh_from_db()
        self.client.force_authenticate(user=self.user)

        # Связная должна быть приятной
        data1 = habits.objects.create(
            id= 333,
            name='Привычка',
            habits_time='2023-11-11T00:00:00Z',
            owner=self.user,
            action='Действие',
            place='Место',
            reward='Вознаграждение',
            period='day',
            nice_habit=False,
            public=False,
            duration=60,
        )
        data1.refresh_from_db()

        data2= {'name': 'Привычка', 'habits_time': '2023-11-11 00:00:00',
                 'action': 'Действие', 'place': 'Место', 'period': 'day',
                 'nice_habit': False, 'public': False, 'duration': 120, 'related_habit': 333}


        response = self.client.post(
            '/habits/create/',
            data=data2
        )
        print(response.json())
        self.assertEquals(response.json(),
        {'non_field_errors':
             ['Связаная привычка всегда приятная. ']
         })


    def test_validation_habits4(self):
        """добавление плохой привычки4"""
        # self.data.save()
        self.client.force_authenticate(user=self.user)
        data = { 'name': 'Привычка', 'habits_time': '2023-11-11 00:00:00',
                'action': 'Действие', 'place': 'Место', 'reward': 'Вознаграждение', 'period': 'day',
                'nice_habit': True, 'public': False, 'duration': 120}


        response = self.client.post(
            '/habits/create/',
            data=data
        )
        self.assertEquals(response.json(), {'non_field_errors': ['У приятной привычки нет вознаграждения. ']})



    def test_validation_habits5(self):
        """добавление плохой привычки5"""

        self.client.force_authenticate(user=self.user)
        data = { 'name': 'Привычка', 'habits_time': '2023-11-11 00:00:00',
                'action': 'Действие', 'place': 'Место', 'reward': 'Вознаграждение', 'period': 'month',
                'nice_habit': False, 'public': False, 'duration': 120}


        response = self.client.post(
            '/habits/create/',
            data=data
        )
        print(response.json())
        self.assertEquals(response.json(), {'non_field_errors':
                                    ['Раз в месяц нельзя только каждый день или раз в неделю. ']})
