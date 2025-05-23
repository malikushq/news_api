from django.urls import path, include
from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import  NewsAdminViewSet, CategoryViewSet, TagsViewSet


router = DefaultRouter()
router.register(r'news',NewsAdminViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'tags',TagsViewSet)

urlpatterns=[
    path('',include(router.urls)),    
]