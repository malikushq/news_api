from django.contrib import admin
from .models import News, Category, Tag


# Register your models here.
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','slug','author','created_at','is_published')
    list_filter = ('is_published','category','tags')
    search_fields = ('title','content','slug')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('tags', )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name', )