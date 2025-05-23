from django.shortcuts import render
from rest_framework import viewsets
from .models import News,Category,Tag
from .serializers import NewsAdminSerializer, CategorySerializer, TagSerializer
from rest_framework.permissions import IsAdminUser


class NewsAdminViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsAdminSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]

class TagsViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUser]