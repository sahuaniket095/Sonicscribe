# Generated by Django 5.0 on 2024-01-30 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Audio', '0003_alter_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='Description',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='Author',
            field=models.CharField(max_length=2000),
        ),
    ]
