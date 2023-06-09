from django.contrib import admin

from .models import Blog, Category





@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", ]
    search_fields = ["name", ]
    list_filter = ["name", ]



@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "blog_subcategory", "base_blog", "views"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "category"]
    list_filter = ["category", "blog_subcategory", "base_blog", "views"]
