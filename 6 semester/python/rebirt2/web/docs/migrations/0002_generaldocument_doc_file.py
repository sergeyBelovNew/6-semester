# Generated by Django 4.2 on 2023-04-17 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='generaldocument',
            name='doc_file',
            field=models.FileField(blank=True, upload_to='doсs'),
        ),
    ]