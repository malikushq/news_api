from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsUserViewSet, news_list_view, news_detail_view, news_list

router = DefaultRouter()
router.register(r'news', NewsUserViewSet, basename='news')

urlpatterns = [
    path('', include(router.urls)),
    path('html/', news_list_view, name='news-html'),
    path('html/<slug:slug>/', news_detail_view, name='news-detail-html'),
    path('cached-news/', news_list, name='news-list-cached'),
]
