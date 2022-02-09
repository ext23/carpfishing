from django.contrib.auth.models import User
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Fish
from .serializers import FishSerializer


def fish_mock_json():
    return {'name': 'Тестовая рыба',
            'description': 'Это тестовое описание тестовой рыбы',
            'logo': '',
            'external_code': '0000001',
            }


def fish_mock_object():
    return Fish.objects.create(
        name='Тестовая рыба',
        description='Это тестовое описание тестовой рыбы',
        external_code='0000001',
        image='')


def test_login():
    return 'testuser'


def test_mail():
    return 'test@user.com'


def test_pass():
    return 'testuserpass'


class CreateFishTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.data = fish_mock_json()

    def test_create_fish(self):
        url = reverse('fishes-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Fish.objects.count(), 1)


class ReadFishTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.fish = fish_mock_object()

    def test_can_read_fish_list(self):
        response = self.client.get(reverse('fishes-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_fish_detail(self):
        response = self.client.get(reverse('fishes-detail', args=[self.fish.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateFishTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.fish = fish_mock_object()
        self.data = FishSerializer(self.fish).data
        self.data.update({'name': 'Карп Карпович', 'image': ''})

    def test_can_update_fish(self):
        response = self.client.put(reverse('fishes-detail', args=[self.fish.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteFishTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.fish = fish_mock_object()

    def test_can_delete_fish(self):
        response = self.client.delete(reverse('fishes-detail', args=[self.fish.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
