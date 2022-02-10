from django.contrib.auth.models import User
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Member
from .serializers import MemberSerializer


def member_mock_json():
    return {'last_name': 'Тестовый',
            'first_name': 'Тест',
            'patronymic': 'Тестович',
            'url_instagram': 'https://instagram.com',
            'external_code': '123'
            }


def member_mock_object():
    return Member.objects.create(
        last_name='Тестовый',
        first_name='Тест',
        patronymic='Тестович',
        url_instagram='https://instagram.com',
        external_code='123')


def test_login():
    return 'testuser'


def test_mail():
    return 'test@user.com'


def test_pass():
    return 'testuserpass'


class CreateMemberTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.data = member_mock_json()

    def test_create_member(self):
        url = reverse('members-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Member.objects.count(), 1)


class ReadMemberTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.member = member_mock_object()

    def test_can_read_member_list(self):
        response = self.client.get(reverse('members-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_member_detail(self):
        response = self.client.get(reverse('members-detail', args=[self.member.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateMemberTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.member = member_mock_object()
        self.data = MemberSerializer(self.member).data
        self.data.update({'first_name': 'Иван',
                          'photo': '', 'scan_id': '',
                          'health_insurance_id': '',
                          'sport_insurance_id': '',
                          'captain_of_team': '',
                          'assistant_of_team': ''})

    def test_can_update_member(self):
        response = self.client.put(reverse('members-detail', args=[self.member.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteMemberTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.member = member_mock_object()

    def test_can_delete_member(self):
        response = self.client.delete(reverse('members-detail', args=[self.member.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
