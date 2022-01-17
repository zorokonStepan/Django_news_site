from django.contrib import admin

from .models import News, Category, Feedback


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "created_at", "updated_at", "is_published", "photo")
    list_display_links = ("id", "title", "category")
    search_fields = ("title", "content")
    list_editable = ("is_published",)
    list_filter = ("is_published", "category")


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
