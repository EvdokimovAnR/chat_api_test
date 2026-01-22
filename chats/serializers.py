from rest_framework import serializers
from .models import Chat, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'text', 'created_at']


class ChatSerializer(serializers.ModelSerializer):
    messages = serializers.SerializerMethodField()

    class Meta:
        model = Chat
        fields = ['id', 'title', 'created_at', 'messages']

    def get_messages(self, obj):
        request = self.context.get('request')
        limit = request.query_params.get('limit', 20) if request else 20

        try:
            limit = int(limit)
            if limit > 100:
                limit = 100
        except:
            limit = 20

        messages = obj.messages.all().order_by('-created_at')[:limit]

        return MessageSerializer(reversed(messages), many=True).data
