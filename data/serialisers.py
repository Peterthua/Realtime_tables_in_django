from rest_framework import serializers
from .models import Post, STATUS


class PostSerialiser(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'

    def get_author(self, obj: Post):
        return obj.author.username

    def get_status(self, obj):
        return STATUS[obj.status][1]
