from rest_framework import serializers
from .models import Paste
from django.contrib.auth.models import User


class PasteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Paste
        fields = '__all__'

    def create(self, validated_data):
        return Paste.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.paste = validated_data.get('paste', instance.paste)
        return instance


class UserSerializer(serializers.ModelSerializer):
    pastes = serializers.PrimaryKeyRelatedField(many=True, queryset=Paste.objects.all())

    class Meta:
        model = User
        fields = '__all__'
