# Generated by Django 5.0 on 2024-02-24 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Audio', '0021_book_ibrary_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='ibrary_users',
        ),
    ]
