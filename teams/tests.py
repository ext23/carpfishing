from django.contrib.auth.models import User
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Team
from .serializers import TeamSerializer


class CreateTeamTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('testuser', 'test@user.com', 'testuserpass')
        self.client.login(username='testuser', password='testuserpass')
        self.data = {'name': 'My Team Гора',
                     'external_code': '00000001',
                     'pin': '0235'}

    def test_create_team(self):
        url = reverse('teams-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Team.objects.count(), 1)


class ReadTeamTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('testuser', 'test@user.com', 'testuserpass')
        self.client.login(username='testuser', password='testuserpass')
        self.team = Team.objects.create(name="My Team Гора",
                                        external_code='00000001',
                                        pin='0235')

    def test_can_read_team_list(self):
        response = self.client.get(reverse('teams-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_team_detail(self):
        response = self.client.get(reverse('teams-detail', args=[self.team.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateTeamTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('testuser', 'test@user.com', 'testuserpass')
        self.client.login(username='testuser', password='testuserpass')
        self.team = Team.objects.create(name="My Team Гора",
                                        external_code='00000001',
                                        pin='0235')
        self.data = TeamSerializer(self.team).data
        self.data.update({'name': 'CARP FISHING 123', 'logo': '', 'captain': '', 'assistant': ''})

    def test_can_update_team(self):
        response = self.client.put(reverse('teams-detail', args=[self.team.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteTeamTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('testuser', 'test@user.com', 'testuserpass')
        self.client.login(username='testuser', password='testuserpass')
        self.team = Team.objects.create(name="My Team Гора",
                                        external_code='00000001',
                                        pin='0235')

    def test_can_delete_team(self):
        response = self.client.delete(reverse('teams-detail', args=[self.team.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
