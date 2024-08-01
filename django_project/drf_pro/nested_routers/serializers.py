from rest_framework.serializers import ModelSerializer
from .models import Author, Post

class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
