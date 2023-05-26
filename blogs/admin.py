from django.contrib import admin

from .models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "created_at"]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
# Register your models here.
