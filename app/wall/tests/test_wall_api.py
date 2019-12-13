from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from core.models import Wall

from wall.serializers import WallSerializer


POST_WALL_URL = reverse('wall:create')
LIST_WALL_URL = reverse('wall:list')


class PublicWallApiTests(TestCase):
    """Test the publicly available Wall API"""

    def setUp(self):
        self.client = APIClient()

    def test_login_not_required(self):
        """Test that login is not required to get request
            on the wall endpoint"""
        Wall.objects.create(
            user=self.user,
            title='Hello World!',
            body='Hello World from inside wall post'
        )
        Wall.objects.create(
            user=self.user,
            title='Hello Universe',
            body='Hello Universe from inside wall post 2'
        )

        res = self.client.get(LIST_WALL_URL)

        posts = Wall.objects.all().order_by('title')
        serializer = WallSerializer(posts, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_login_required(self):
        """Test that login is required to post request on the wall endpoint"""
        payload = {
            'title': 'Hello World!',
            'body': 'Hello World from inside wall post'
            }
        res = self.client.post(POST_WALL_URL, payload)

        exists = Wall.objects.filter(
            user=self.user,
            title=payload['title'],
        ).exists()
        self.assertFalse(exists)
        self.assertEqual(res.status, status.HTTP_401_UNAUTHORIZED)


class PrivateWallApiTests(TestCase):
    """Test Wall can be posted by authorized user"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@email.com',
            'testpass'
        )
        self.client.force_authenticate(self.user)

    def test_login_not_required(self):
        """Test that login is not required to
            get request on the wall endpoint"""
        Wall.objects.create(
            user=self.user,
            title='Hello World!',
            body='Hello World from inside wall post'
        )
        Wall.objects.create(
            user=self.user,
            title='Hello Universe',
            body='Hello Universe from inside wall post 2'
        )

        res = self.client.get(LIST_WALL_URL)

        posts = Wall.objects.all().order_by('title')
        serializer = WallSerializer(posts, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_post_on_wall_successful(self):
        """Test create a new post on wall"""
        payload = {
            'title': 'Hello World!',
            'body': 'Hello World from inside wall post'
            }
        self.client.post(POST_WALL_URL, payload)

        exists = Wall.objects.filter(
            user=self.user,
            title=payload['title'],
        ).exists()
        self.assertTrue(exists)

    def test_post_on_wall_invalid(self):
        """Test creating invalid posts on wall fails"""
        payload = {'title': '', 'body': ''}
        res = self.client.post(POST_WALL_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
