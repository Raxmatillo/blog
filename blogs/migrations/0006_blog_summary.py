# Generated by Django 4.2 on 2023-06-09 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_alter_blog_blog_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.CharField(default=2, max_length=300, verbose_name='Qisqacha'),
            preserve_default=False,
        ),
    ]
