# Generated by Django 5.0 on 2024-02-05 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Audio', '0006_remove_book_pdf_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pdf_file',
            field=models.FileField(default=2, upload_to='static/dist'),
            preserve_default=False,
        ),
    ]
