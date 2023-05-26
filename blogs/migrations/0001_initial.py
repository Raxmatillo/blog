# Generated by Django 4.2 on 2023-05-26 05:45

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name="Bo'lim nomi")),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Blog nomi')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Blog matni')),
                ('slug', models.SlugField(max_length=200, null=True, verbose_name='URL')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(null='Boshqa', on_delete=django.db.models.deletion.SET_NULL, to='blogs.category')),
                ('owner', models.ForeignKey(null="O'chirilgan hisob", on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Blog',
                'verbose_name_plural': 'Bloglar',
                'db_table': 'blogs',
                'ordering': ['-created_at'],
            },
        ),
    ]
