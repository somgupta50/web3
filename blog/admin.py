from django.contrib import admin
from .models import Article, Tag, Subscriber


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','slug','created_on')

admin.site.register(Tag)

admin.site.register(Subscriber)