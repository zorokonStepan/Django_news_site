from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import News, Category, Feedback


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "created_at", "updated_at", "is_published", "get_photo")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ("is_published",)
    list_filter = ("is_published", "category")
    fields = ('title', 'category', 'content', 'photo', 'is_published', 'get_photo', 'views', 'created_at', 'updated_at')
    readonly_fields = ('get_photo', 'views', 'created_at', 'updated_at')
    save_on_top = True

    def get_photo(self, obj):
        if obj.photo:
            # проверка на случай отсутствия картинки в записи
            return mark_safe(f'<img src="{obj.photo.url}" width="30">')
        return 'фото не установлено'

    get_photo.short_description = "Миниатюра"


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "contact", "message")
    list_display_links = ("id", "name", "contact", "message")
    search_fields = ("name",)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Feedback, FeedbackAdmin)

admin.site.site_title = "Управление новостями"
admin.site.site_header = "Управление новостями"
