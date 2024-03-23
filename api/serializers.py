from django.db import transaction
from rest_framework import serializers
from api.models import Entry, User


class UserSerializer(serializers.ModelSerializer):
    last_entry = serializers.SerializerMethodField()
    total_message_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['name', 'last_entry', 'total_message_count']

    def get_total_message_count(self, instance):
        total_count = instance.entries.count()
        return total_count

    def get_last_entry(self, instance):
        last_entry = instance.entries.order_by('-created_at').first()
        if last_entry:
            return f"{last_entry.subject} | {last_entry.message}"
        return None


class EntrySerializer(serializers.ModelSerializer):
    name = serializers.CharField(write_only=True, required=True)
    user = serializers.SerializerMethodField()

    class Meta:
        model = Entry
        fields = ['name', 'subject', 'message', 'user']

    def get_user(self, instance):
        return instance.user.name

    @transaction.atomic
    def create(self, validated_data):
        name = validated_data.pop('name')
        user_serializer = UserSerializer(data={'name': name})
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        entry = Entry.objects.create(
            **validated_data, user=user
        )
        return entry
