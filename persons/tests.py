from django.contrib.auth.models import User
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Person
from .serializers import PersonSerializer


def person_mock_json():
    user = User.objects.get(username=test_login())

    return {'last_name': 'Тестовый',
            'first_name': 'Тест',
            'user': user.id,
            'external_code': '123'
            }


def person_mock_object():
    user = User.objects.get(username=test_login())

    return Person.objects.create(
        last_name='Тестовый',
        first_name='Тест',
        user=user,
    )


def test_login():
    return 'testuser'


def test_mail():
    return 'test@user.com'


def test_pass():
    return 'testuserpass'


class CreatePersonTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.data = person_mock_json()

    def test_create_person(self):
        url = reverse('persons-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)


class ReadPersonTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.person = person_mock_object()

    def test_can_read_person_list(self):
        response = self.client.get(reverse('persons-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_person_detail(self):
        response = self.client.get(reverse('persons-detail', args=[self.person.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdatePersonTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.person = person_mock_object()
        self.data = PersonSerializer(self.person).data
        self.data.update({'first_name': 'Иван',
                          'photo': ''})

    def test_can_update_person(self):
        response = self.client.put(reverse('persons-detail', args=[self.person.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeletePersonTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.person = person_mock_object()

    def test_can_delete_person(self):
        response = self.client.delete(reverse('persons-detail', args=[self.person.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
