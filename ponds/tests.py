from django.contrib.auth.models import User
from django.urls import include, path, reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Pond, Sector
from .serializers import PondSerializer, SectorSerializer


def pond_mock_json():
    return {'name': 'Тестовый водоем',
            'zone': 'A01',
            'width_bottom': '1234.123',
            'width_top': '5231.123',
            'max_depth': '123.555',
            'avg_depth': '999.111',
            'square': '555.555',
            'fish_density': '124124.212',
            'avg_fish_weight': '124.222',
            'description': 'Тестовый водоем на test территории',
            'address': 'Test ',
            'sector_width': '555.55',
            'cell_height': '20',
            'sectors': []
            }


def sector_mock_json(pond):
    return {
        'pond': pond,
        'number': 1,
    }


def pond_mock_object():
    return Pond.objects.create(
        name='Тестовый водоем', zone='A01',
        width_bottom=1234.123, width_top=5231.123,
        max_depth=123.555, avg_depth=999.111,
        square=555.555, fish_density=124124.212,
        avg_fish_weight=124.222, description='Тестовый водоем на test территории',
        address='Test ',
        sector_width=555.55, cell_height=20,
        logo='')


def sector_mock_object(pond):
    return Sector.objects.create(
        pond=pond, number=1,
    )

def test_login():
    return 'testuser'


def test_mail():
    return 'test@user.com'


def test_pass():
    return 'testuserpass'


class CreatePondTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.data = pond_mock_json()

    def test_create_pond(self):
        url = reverse('ponds-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pond.objects.count(), 1)


class ReadPondTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.pond = pond_mock_object()

    def test_can_read_pond_list(self):
        response = self.client.get(reverse('ponds-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_pond_detail(self):
        response = self.client.get(reverse('ponds-detail', args=[self.pond.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdatePondTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.pond = pond_mock_object()
        self.data = PondSerializer(self.pond).data
        self.data.update({'name': 'Водоем123', 'logo': ''})

    def test_can_update_pond(self):
        response = self.client.put(reverse('ponds-detail', args=[self.pond.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeletePondTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.pond = pond_mock_object()

    def test_can_delete_team(self):
        response = self.client.delete(reverse('ponds-detail', args=[self.pond.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CreateSectorTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.pond = pond_mock_object()
        self.data = sector_mock_json(pond=self.pond.id)

    def test_create_sector(self):
        url = reverse('sectors-list')
        response = self.client.post(url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sector.objects.count(), 1)


class ReadSectorTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.pond = pond_mock_object()
        self.sector = sector_mock_object(pond=self.pond)

    def test_can_read_sector_list(self):
        response = self.client.get(reverse('sectors-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_read_sector_detail(self):
        response = self.client.get(reverse('sectors-detail', args=[self.sector.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class UpdateSectorTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.pond = pond_mock_object()
        self.sector = sector_mock_object(self.pond)
        self.data = SectorSerializer(self.sector).data
        self.data.update({'number': 50,})

    def test_can_update_sector(self):
        response = self.client.put(reverse('sectors-detail', args=[self.sector.id]), self.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeleteSectorTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(test_login(), test_mail(), test_pass())
        self.client.login(username=test_login(), password=test_pass())
        self.pond = pond_mock_object()
        self.sector = sector_mock_object(self.pond)

    def test_can_delete_sector(self):
        response = self.client.delete(reverse('sectors-detail', args=[self.sector.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
