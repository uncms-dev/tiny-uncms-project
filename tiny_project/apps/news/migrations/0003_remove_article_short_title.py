# Generated by Django 3.2.15 on 2022-10-08 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_article_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='short_title',
        ),
    ]