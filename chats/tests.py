from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Chat, Message


class ChatAPITests(APITestCase):
    def setUp(self):
        self.chat = Chat.objects.create(title='Тестовый чат')

    def test_create_chat_success(self):
        url = reverse('chat-list')
        data = {'title': 'Новый чат'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Chat.objects.count(), 2)

    def test_create_chat_empty_title(self):
        url = reverse('chat-list')
        data = {'title': '  '}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_message_success(self):
        url = reverse('chat-messages', args=[self.chat.id])
        data = {'text': 'Тестовое сообщение'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Message.objects.count(), 1)


