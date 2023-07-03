from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

from froala_editor.fields import FroalaField





blog_subcategory = (
    ('blog', 'Blog'),
    ('project', 'Loyiha')
    )



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
    summary = models.CharField(max_length=300, verbose_name="Qisqacha")
    body = FroalaField(options={
      'toolbarInline': False,
    })
    photo = models.ImageField(upload_to="images/", verbose_name="Blog post rasmi", default='blog.png')
    slug = models.SlugField(max_length=200, null=True, verbose_name='URL')
    blog_subcategory = models.CharField(max_length=50, choices = blog_subcategory, default='blog', verbose_name="Subkategoriya")
    base_blog = models.BooleanField(default=False, verbose_name="Asosiy blog")
    views = models.IntegerField(default=0, null=True, blank=True, verbose_name="Ko'rishlar soni")
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