from rest_framework import serializers
from .models import News, Category, Tag
from django.contrib.auth.models import User

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']

class NewsAdminSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only = True)

    class Meta:
        model = News
        fields = ['id','title','content','slug','author','created_at','updated_at','tags','category','is_published']