from django.contrib.auth.models import Group, User
from rest_framework import serializers

from .models import Note


class UserSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class NoteSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'contents']
