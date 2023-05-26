from rest_framework.serializers import ModelSerializer, SlugField

from blogs.models import Blog, Category
from django.contrib.auth.models import User


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class BlogSerializer(ModelSerializer):
    owner = UserSerializer()
    category = CategorySerializer()

    # slug = SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='name'
    # )
    slug = SlugField()
    class Meta:
        model = Blog
        fields = ['id', 'owner', 'category', 'title', 'body', 'slug',
        'created_at', 'updated_at']
        depth = 1
        # lookup_field = 'slug'
        # extra_kwargs = {
        #     'id': {'lookup_field': 'slug'}
        # }