from django.contrib.auth.models import User

from rest_framework import serializers

from blogs.models import Category, Blog



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'options')


class BlogSerializer(serializers.ModelSerializer):
    owner = UserSerializer()
    class Meta:
        model = Blog
        fields = ('id', 'owner', 'category', 'title', 'summary', 'body', 'photo', 'blog_subcategory', 'slug', 'base_blog', 'views', 'created_at')
        depth = 2
