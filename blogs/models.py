from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



class Category(models.Model):
    name = models.CharField(max_length=120, verbose_name="Bo'lim nomi")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Bo'lim"
        verbose_name_plural="Bo'limlar"
        db_table = "category"


class Blog(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,
                              null="O'chirilgan hisob")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null="Boshqa")
    title = models.CharField(max_length=150, verbose_name="Blog nomi")
    body = RichTextUploadingField(verbose_name="Blog matni")
    slug = models.SlugField(max_length=200, null=True, verbose_name='URL')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name="Blog"
        verbose_name_plural = "Bloglar"
        ordering = ['-created_at']
        db_table = "blogs"