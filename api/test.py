# tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User, Entry


class GuestBookTest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_entry(self):
        response = self.client.post('/api/guest-book/', {
            'name': 'John',
            'subject': 'Test Subject',
            'message': 'Test Message'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Entry.objects.count(), 1)

    def test_get_entries(self):
        user = User.objects.create(name='Jane')
        Entry.objects.create(user=user, subject='Subject 1', message='Message 1')
        Entry.objects.create(user=user, subject='Subject 2', message='Message 2')

        response = self.client.get('/api/guest-book/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 2)

    def test_get_users_data(self):
        user1 = User.objects.create(name='User1')
        Entry.objects.create(user=user1, subject='Subject 1', message='Message 1')

        user2 = User.objects.create(name='User2')
        Entry.objects.create(user=user2, subject='Subject 2', message='Message 2')

        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
