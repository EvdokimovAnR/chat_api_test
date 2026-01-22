from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import NotFound


class ChatViewSet(viewsets.ModelViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def create(self, request, *args, **kwargs):
        """Создать чат (POST /chats/)"""
        title = request.data.get('title', '').strip()
        if not title:
            return Response({'error': 'Заголовок не может быть пустым'}, status=status.HTTP_400_BAD_REQUEST)
        if len(title) > 200:
            return Response({'error': "Заголовок не может превышать 200 символов"}, status=status.HTTP_400_BAD_REQUEST)
        chat = Chat.objects.create(title=title)
        return Response(ChatSerializer(chat).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def messages(self, request, pk=None):
        try:
            chat = Chat.objects.get(id=pk)
        except Chat.DoesNotExist:
            raise NotFound("Чат не найден")

        text = request.data.get('text', '').strip()
        if not text:
            return Response({'error': 'Текст не может быть пустым'}, status=status.HTTP_400_BAD_REQUEST)
        if len(text) > 5000:
            return Response({'error': 'Текст сообщения не может превышать 5000 символов'}, status=status.HTTP_400_BAD_REQUEST)
        message = Message.objects.create(chat=chat, text=text)
        return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        """Удалить чат (DELETE /chats/{id}/)"""
        # Django сам удалит все сообщения благодаря on_delete=models.CASCADE
        chat = self.get_object()
        chat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
