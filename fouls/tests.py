from django.contrib.auth.models import User
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Foul
from .serializers import FoulSerializer


def foul_mock_json():
    return {'name': 'Тестовое нарушение',
            'decision': 'WR',
            'external_code': '0000001',
            }


def foul_mock_object():
    return Foul.objects.create(
        name='Тестовое нарушение',
        decision='WR',
        external_code='0000001',
    )


def test_login():
    return 'testuser'


def test_mail():
    return 'test@user.com'


def test_pass():
    return 'testuserpass'


class CreateFoulTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.data = foul_mock_json()

    def test_create_foul(self):
        url = reverse('fouls-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Foul.objects.count(), 1)


class ReadFoulTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.foul = foul_mock_object()

    def test_can_read_foul_list(self):
        response = self.client.get(reverse('fouls-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_foul_detail(self):
        response = self.client.get(reverse('fouls-detail', args=[self.foul.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateFoulTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.foul = foul_mock_object()
        self.data = FoulSerializer(self.foul).data
        self.data.update({'name': 'Грубое нарушение'})

    def test_can_update_foul(self):
        response = self.client.put(reverse('fouls-detail', args=[self.foul.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteFoulTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.foul = foul_mock_object()

    def test_can_delete_fish(self):
        response = self.client.delete(reverse('fouls-detail', args=[self.foul.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
