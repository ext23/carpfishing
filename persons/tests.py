from django.contrib.auth.models import User
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Person, Member, Judge
from .serializers import PersonSerializer, MemberSerializer, JudgeSerializer


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


def member_mock_json():
    user = User.objects.get(username=test_login())

    person = Person.objects.create(
        last_name='Тестовый',
        first_name='Тест',
        user=user,
    )

    return {'person': person.id,
            'url_instagram': 'https://instagram.com',
            'external_code': '123',
            }


def member_mock_object():
    user = User.objects.get(username=test_login())

    person = Person.objects.create(
        last_name='Тестовый',
        first_name='Тест',
        user=user,
    )

    return Member.objects.create(
        person=person,
        url_instagram='https://instagram.com',
        external_code='123')


def judge_mock_json():
    user = User.objects.get(username=test_login())

    person = Person.objects.create(
        last_name='Тестовый',
        first_name='Тест',
        user=user,
    )

    return {'position': 'Судья',
            'person': person.id}


def judge_mock_object():
    user = User.objects.get(username=test_login())

    person = Person.objects.create(
        last_name='Тестовый',
        first_name='Тест',
        user=user,
    )

    return Judge.objects.create(
        person=person,
        position='Помощник судьи')


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


class CreateJudgeTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.data = judge_mock_json()

    def test_create_judge(self):
        url = reverse('judges-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Judge.objects.count(), 1)


class ReadJudgeTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.judge = judge_mock_object()

    def test_can_read_judge_list(self):
        response = self.client.get(reverse('judges-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_judge_detail(self):
        response = self.client.get(reverse('judges-detail', args=[self.judge.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateJudgeTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.judge = judge_mock_object()
        self.data = JudgeSerializer(self.judge).data
        self.data.update({'position': 'Судья',
                          'facsimile': ''})

    def test_can_update_judge(self):
        response = self.client.put(reverse('judges-detail', args=[self.judge.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteJudgeTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.judge = judge_mock_object()

    def test_can_delete_judge(self):
        response = self.client.delete(reverse('judges-detail', args=[self.judge.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
